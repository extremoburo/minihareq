from mhqueue.tasks import run, runJob
from time import sleep
from tqdm import tqdm 

clis_lines = []

with open("mhqueue/inputs/clis.txt", 'r') as clis:
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

