from app import run_pipeline
from apscheduler.schedulers.blocking import BlockingScheduler

def start():
    scheduler=BlockingScheduler()
    run_pipeline()

    scheduler.add_job(run_pipeline, "interval", minutes=1)

    scheduler.start()