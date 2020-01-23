result_expires=60
task_acks_late=True
broker_url='pyamqp://'
result_backend='redis://localhost'
task_serializer='json'
include=['queue.tasks']
