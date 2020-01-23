from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('mhqueue')

# module celecyconfig.py in the same dir 
app.config_from_object('mhqueue.celeryconfig')


if __name__ == '__main__':
    app.start()