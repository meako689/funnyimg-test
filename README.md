funnyimg-test
=============

Simple web-app that shows you funny pictures from instagram and tumblr

written with flask and angular-js

Fun, unreliable very inefficent and irrational.

To set-up:

get yourself some virtualenv:
```
pip install requirements
python manage.py syncdb
python manage.py runserver
```
set proper values in config.local (instagram and tumblr auth)
go to http://127.0.0.1:5000 and enjoy!

Tests:
```
nosetests
```


