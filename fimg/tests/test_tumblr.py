"""Test creating db model from tumblr response"""
import json

from nose.tools import *

from fimg import db
from fimg import app

from .tumblr_response import response
from ..tasks import parse_tumblr
from ..models import FunnyImage

test_client = app.test_client()

def setup():
    db.create_all()

def teardown():
    db.drop_all()

def test_from_response():
    """
    pass
    """
    parse_tumblr(response)
    eq_(FunnyImage.query.count(),16)
    photo = FunnyImage.query.get(1)

    resp_item = filter(lambda i:i['type'] == 'photo',response)[0]
    eq_(photo.img_url,
            resp_item['photos'][0]['original_size']['url'])
    eq_(photo.description,
            resp_item['caption'])
    FunnyImage.query.delete()


def test_api_photos_list():
    """docstring for test_api_photos_list"""
    eq_(FunnyImage.query.count(),0)
    parse_tumblr(response)
    rv = test_client.get('/photostream/')
    eq_(rv.status_code, 200)
    resp = json.loads(rv.data)
    eq_(len(resp),16)
    resp_item = resp[0]
    photo = FunnyImage.query.get(1)
    eq_(photo.img_url,
            resp_item['img_url'])
    eq_(photo.description,
            resp_item['description'])


