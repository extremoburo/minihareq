from celery import group
from proj.celery import app

@app.task
def add(x, y):
    return x + y

@app.task
def master():
    return group(add.s(1, 2), add.s(3, 4))()