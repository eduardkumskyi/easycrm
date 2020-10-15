from apiconnections.novaposhta import np_status_update_all
from EasyCRM.celery import app


@app.task
def periodic_np_status_update_all():
    np_status_update_all()
