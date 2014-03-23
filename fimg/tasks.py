import datetime

from fimg import db

from .models import FunnyImage
 
def parse_tumblr(response):
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




