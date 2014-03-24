import time
import datetime
import pytumblr

from fimg import app
from fimg import db

from .models import FunnyImage
 
class TumblrLoader(object):
    """Wrapper on tumblr's api wrapper"""
    def __init__(self):
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
                    vendor = 'tumblr',
                    vendor_id=item['id'],
                    vendor_url = item['post_url'],
                    posted_at = datetime.datetime.fromtimestamp(item['timestamp'])
            )
            db.session.add(photo)
        db.session.commit()

    def load_tagged(self, tag, before=None):
        """load tagged items into db"""
        response = self.client.tagged(tag,filter='text',before=before)
        self.parse_response(response)

    def load_older_entries(self,tag):
        """load more entries that we have in db"""
        if FunnyImage.query.count():
            oldestentry = FunnyImage.query.order_by(FunnyImage.posted_at.asc())[0]
            timestamp = int(time.mktime(oldestentry.posted_at.timetuple()))
        else:
            timestamp = int(time.time())
        self.load_tagged(tag,timestamp) 

