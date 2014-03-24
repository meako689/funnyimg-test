from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with

from fimg import app

from .models import FunnyImage
from .datasources import TumblrLoader, InstagramLoader
 
api = restful.Api(app)

class FunnyImgResource(restful.Resource):
    def __init__(self):
        super(FunnyImgResource,self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('limit', type=int)
        self.parser.add_argument('offset', type=int)
        self.tl = TumblrLoader()
        self.il = InstagramLoader()

    mfields = {
            'img_url':fields.Raw,
            'description':fields.Raw,
            'vendor_url':fields.Raw
    }
            
    @marshal_with(mfields)
    def get(self, **kwargs):
        reqargs = self.parser.parse_args()
        limit = reqargs.get('limit')
        if not limit: limit = 20

        offset = reqargs.get('offset')
        if offset == FunnyImage.query.count():
            tag = 'lol'
            self.tl.load_older_entries(tag)
            self.il.load_older_entries(tag)

        photos = FunnyImage.query.limit(limit).offset(offset).all()
        return photos

api.add_resource(FunnyImgResource, '/photostream/')
