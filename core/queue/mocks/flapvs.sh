# simulate the exection of a client processing some tasks 
# usage: ./flapvs.sh number_of_tasks

#!/bin/bash 

if [ -z "$1" ]
then
  echo "provide the task number"
  exit 1
fi

echo "starting flapvs mock"
task_count=1
tasks=$1
i=1

until [ $i -gt $tasks ]
do
  echo task $i
  sleep 1
  ((i=i+1))
done
