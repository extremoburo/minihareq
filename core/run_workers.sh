#!/bin/bash 

# convenience scrypt to run celery worker
celery -A mhqueue worker -l info --concurrency=2
