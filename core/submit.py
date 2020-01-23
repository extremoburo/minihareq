from celeryproj.tasks import run, runJob, add
from celery import group
from celery.result import ResultBase
from time import sleep
from tqdm import tqdm 

clis_lines = []

with open("celeryproj/inputs/clis.txt", 'r') as clis:
    count = 1
    for cli in clis: 
        # skip commented lines
        if not '#' in cli:
            clis_lines.append((cli,count))
            count += 1

print("Inputs:", clis_lines)
result = runJob(clis_lines)

total = len(clis_lines)

while result.completed_count() != total:
    sleep(2)
    globalres = [res for res in result.results]
    for res in globalres:
        print("ID: ", res.id)
        print("STATE: ", res.state)
        #print("INFO: ", res.info)

    print("completed: ", result.completed_count())

print(result.get())
result.forget()

#result = run.delay(clis_lines[0])
# while not result.ready():
#     print("check results")
#     print(result.ready())

#results = []
#for result in tqdm(result_group.children[0], total=30):
#    results.append(result.get())
#print(results)

#print(result.collect())
#print(result.id)
#print(result.get())

#results = run.delay(['ls', '/tmp'])
#results = run.apply_async((["ls", "/tmp"], countdown=3)
#print("READY:", results.ready())

