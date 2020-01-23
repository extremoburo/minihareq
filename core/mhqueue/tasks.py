from __future__ import absolute_import, unicode_literals
from .celery import app
from celery import group
import subprocess


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
        return { 'retcode': 1, 'pos': pos, 'state': 'failed' }

