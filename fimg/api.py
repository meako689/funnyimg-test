from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with

from fimg import app

from .models import FunnyImage
 
api = restful.Api(app)

class FunnyImgResource(restful.Resource):
    mfields = {
            'img_url':fields.Raw,
            'description':fields.Raw,
            'vendor_url':fields.Raw
    }
            
    @marshal_with(mfields)
    def get(self, **kwargs):
        photos = FunnyImage.query.all()
        return photos

api.add_resource(FunnyImgResource, '/photostream/')
