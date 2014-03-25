Funnyimg-test
=============

Simple web-app that shows you funny pictures from instagram and tumblr

View live:http://funnyimg.herokuapp.com/

written with flask and angular-js

Fun, unreliable very inefficent and irrational.

##Set-up:

get yourself some virtualenv or [vagrant env](https://github.com/meako689/vagrant-puppet-django):
```
pip install -r requirements.txt
python manage.py syncdb
```
set proper values in config/local.py or ENV (instagram and tumblr auth)
```
python manage.py runserver
```

go to http://127.0.0.1:5000 and enjoy!

##Tests:
```
nosetests
```

##
