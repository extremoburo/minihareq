from __future__ import absolute_import, unicode_literals
from .celery import app
from celery import group
from celery.exceptions import CeleryError, SoftTimeLimitExceeded 
import subprocess
from time import sleep

# store the process position when a timeout is caught 
def store_process(position):
    print("store somewhere pos: ", position)

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

        retcode = subprocess.run(subproc_cmd, stdout=True, stderr=True, check=True).returncode
        return { 'retcode': retcode, 'pos': pos, 'state': 'completed' }
  
    except subprocess.CalledProcessError as e: 
        print("errore di subprocess", e.stderr)
        # this doesn't work as expected as it stops celery task
        #raise CeleryError
        return { 'retcode': 1, 'pos': pos, 'state': 'failed' }
    
    except SoftTimeLimitExceeded:
        store_process(pos)

@app.task
def test():
    try:
        print("sleeping...")
        sleep(3)
        return "finito"
    except SoftTimeLimitExceeded:
        print("gestione soft")