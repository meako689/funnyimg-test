from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with

from fimg import app

from .models import FunnyImage
from .datasources import TumblrLoader
 
api = restful.Api(app)
tl = TumblrLoader()

class FunnyImgResource(restful.Resource):
    def __init__(self):
        super(FunnyImgResource,self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('limit', type=int)
        self.parser.add_argument('offset', type=int)

    mfields = {
            'img_url':fields.Raw,
            'description':fields.Raw,
            'vendor_url':fields.Raw
    }
            
    @marshal_with(mfields)
    def get(self, **kwargs):
        reqargs = self.parser.parse_args()
        limit = reqargs.get('limit', 20)
        offset = reqargs.get('offset')
        if offset == FunnyImage.query.count():
            print "loaded"
            tl.load_older_entries('fun')

        photos = FunnyImage.query.limit(limit).offset(offset).all()
        return photos

api.add_resource(FunnyImgResource, '/photostream/')
