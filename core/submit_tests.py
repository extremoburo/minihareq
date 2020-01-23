from celeryproj.tasks import bindtest
from celery import group
from celery.result import ResultBase

def on_raw_message(body):
    print(body)

a, b = 1, 1
r = bindtest.apply_async(args=(a, b))
print(r.get(on_message=on_raw_message, propagate=False))