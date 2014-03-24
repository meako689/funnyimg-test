import time
import datetime
import pytumblr

from instagram.client import InstagramAPI

from fimg import app
from fimg import db

from .models import FunnyImage
 
class ApiLoader(object):
    def load_older_entries(self,tag):
        """load more entries that we have in db"""

        items = FunnyImage.query.order_by(
                    'posted_at asc').filter_by(vendor=self.vendor)
        if items.count():
            oldestentry = items[0]
            timestamp = int(time.mktime(oldestentry.posted_at.timetuple()))
        else:
            timestamp = int(time.time())
        self.load_tagged(tag,timestamp)

class InstagramLoader(ApiLoader):
    """Wrapper on instagram api"""
    def __init__(self):
        self.client =  InstagramAPI(access_token=app.config['INSTAGRAM']['token'])
        self.vendor = "instagram"

    def parse_response(self, response):
        """docstring for parse_instagram"""
        photos = response[0]
        for item in photos:
            photo = FunnyImage(
                    img_url=item.get_standard_resolution_url(),
                    description=item.caption.text if item.caption else '',
                    vendor = self.vendor,
                    vendor_id=item.id,
                    vendor_url = item.link,
                    posted_at = item.created_time,
            )
            db.session.add(photo)
        db.session.commit()

    def load_tagged(self, tag, timestamp=None):
        result = self.client.tag_recent_media(20, timestamp, tag)
        self.parse_response(result)



class TumblrLoader(ApiLoader):
    """Wrapper on tumblr's api wrapper"""
    def __init__(self):
        self.vendor = "tumblr"
        self.client = pytumblr.TumblrRestClient(
                app.config['TUMBLR']['key'],
                app.config['TUMBLR']['secret'],
                app.config['TUMBLR']['token'],
                app.config['TUMBLR']['token_secret'],
        )

    def parse_response(self, response):
        """Create db models, based on response from api"""
        photos = filter(lambda i:i['type'] == 'photo',response)
        for item in photos:
            photo = FunnyImage(
                    img_url=item['photos'][0]['original_size']['url'],
                    description=item['caption'],
                    vendor = self.vendor,
                    vendor_id=item['id'],
                    vendor_url = item['post_url'],
                    posted_at = datetime.datetime.fromtimestamp(item['timestamp'])
            )
            db.session.add(photo)
        db.session.commit()

    def load_tagged(self, tag, timestamp=None):
        """load tagged items into db"""
        response = self.client.tagged(tag,filter='text',before=timestamp)
        self.parse_response(response)
