from celery import Celery
import time
app = Celery('celery_app', broker='redis://localhost:6379/1',backend="rpc://")

@app.task
def delay_one_min():
    print("Executing delay_one_min")
    time.sleep(60)
    return "success"


