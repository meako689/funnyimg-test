"""Test creating db model from tumblr response"""
import json

from nose.tools import *

from fimg import db
from fimg import app

from .data.tumblr_example_response import tumblr_response
from .data.instagram_example_response import instagram_response
from ..datasources import TumblrLoader, parse_instagram
from ..models import FunnyImage

test_client = app.test_client()
tumblrr = TumblrLoader()

def setup():
    db.create_all()

def teardown():
    db.drop_all()

def test_from_tumblr_response():
    """
    pass
    """
    eq_(FunnyImage.query.count(),0)
    tumblrr.parse_response(tumblr_response)
    eq_(FunnyImage.query.count(),16)
    photo = FunnyImage.query.get(1)

    resp_item = filter(lambda i:i['type'] == 'photo',tumblr_response)[0]
    eq_(photo.img_url,
            resp_item['photos'][0]['original_size']['url'])
    eq_(photo.description,
            resp_item['caption'])
    FunnyImage.query.delete()


def test_from_instagram_response():
    """docstring for test_from_instagram_response"""
    eq_(FunnyImage.query.count(),0)
    parse_instagram(instagram_response)
    eq_(FunnyImage.query.count(),10)
    photo = FunnyImage.query.all()[0]
    res_item = instagram_response[0][0]

    eq_(photo.img_url,res_item.images['standard_resolution'].url)
    eq_(photo.description,res_item.caption.text)
    eq_(photo.vendor,'instagram')
    eq_(photo.vendor_id,res_item.id)
