from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('queue')

# module celecyconfig.py in the same dir 
app.config_from_object('queue.celeryconfig')

if __name__ == '__main__':
    app.start()