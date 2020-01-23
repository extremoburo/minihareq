from mhqueue.tasks import test

res = test.delay()
print(res.get())

res2 = test.apply_async(countdown=5, soft_time_limit=1)
print(res2.get())