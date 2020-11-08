from huey import crontab
from huey.contrib.djhuey import periodic_task, task

from apiconnections.novaposhta import np_state_update_all


# @task()
# def count_beans(number):
#     print('-- counted %s beans --' % number)
#     return 'Counted %s beans' % number

@periodic_task(crontab(minute='*/1'))
def periodic_np_state_update_all():
    np_state_update_all()
