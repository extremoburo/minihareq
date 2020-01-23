#!/bin/bash 

# convenience scrypt to run celery worker
celery -A celeryproj worker -l info --concurrency=2
