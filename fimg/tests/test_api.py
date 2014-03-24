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
 
def test_api_photos_list():
    """docstring for test_api_photos_list"""
    eq_(FunnyImage.query.count(),0)
    tumblrr.parse_response(response)
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

    rv = test_client.get('/photostream/?limit=4&offset=5')
    eq_(rv.status_code, 200)
    new_resp = json.loads(rv.data)
    eq_(len(new_resp),4)
    eq_(new_resp[0],resp[5])
    eq_(new_resp[3],resp[8])

