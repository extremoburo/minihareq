from __future__ import absolute_import, unicode_literals
from .celery import app
from celery import group
from time import sleep
import subprocess

@app.task
def add(x, y):
    return x + y

@app.task
def runJob(tasks):
    return group(run.s(task, pos) for task, pos in tasks)()

@app.task
def run(cmd, pos):
    try:
        subproc_cmd = cmd.split()
        # with (bind=True) for debugging purporse
        # print('Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(
        # self.request))

        execDescr = subprocess.run(subproc_cmd, stdout=True, stderr=True)
        return { 'retcode': execDescr.returncode, 'pos': pos, 'state': 'completed' }
  
    except subprocess.CalledProcessError as e: 
        print("errore di subprocess", e.stderr)
        return { 'retcode': 1, 'pos': pos, 'state': 'failed' }
    #except:
    #    return { 'retcode': 2, 'pos': pos, 'state': 'failed' }

# example for collect() 
@app.task
def A(how_many):
    return group(B.s(i) for i in range(how_many))()

@app.task
def B(i):
    return pow2.delay(i)

@app.task(trail=True)
def pow2(i):
    return i ** 2

@app.task(bind=True)
def bindtest(self, a, b):
    sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    sleep(1)
    return 'hello world: %i' % (a+b)