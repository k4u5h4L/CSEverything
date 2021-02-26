from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from .getLiveScore import update_match


def simply_print():
    print(f'scheduled task')

        
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_match, 'interval', minutes=0.1)
    # scheduler.start()