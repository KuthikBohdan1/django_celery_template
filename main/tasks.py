from celery import Task, shared_task
from {{ project_name }}.celery import app

@app.task()
def hi_task():
    print("hi from")