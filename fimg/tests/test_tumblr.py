"""Test creating db model from tumblr response"""
from nose.tools import *

from fimg import db
from fimg import app

from .tumblr_response import response
from ..tasks import parse_tumblr
from ..models import FunnyImage

def setup():
    db.create_all()

def test_from_response():
    """
    pass
    """
    parse_tumblr(response)
    eq_(FunnyImage.query.count(),16)
    photo = FunnyImage.query.get(1)
    resp_item = response[0]
    eq_(photo.img_url,
            resp_item['photos'][0]['original_size']['url'])
    eq_(photo.description,
            resp_item['caption'])

    import ipdb; ipdb.set_trace()
