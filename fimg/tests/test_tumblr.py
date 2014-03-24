"""Test creating db model from tumblr response"""
import json

from nose.tools import *

from fimg import db
from fimg import app

from .data.tumblr_example_response import response
from ..datasources import TumblrLoader
from ..models import FunnyImage

test_client = app.test_client()
tumblrr = TumblrLoader()

def setup():
    db.create_all()

def teardown():
    db.drop_all()

def test_from_response():
    """
    pass
    """
    tumblrr.parse_response(response)
    eq_(FunnyImage.query.count(),16)
    photo = FunnyImage.query.get(1)

    resp_item = filter(lambda i:i['type'] == 'photo',response)[0]
    eq_(photo.img_url,
            resp_item['photos'][0]['original_size']['url'])
    eq_(photo.description,
            resp_item['caption'])


