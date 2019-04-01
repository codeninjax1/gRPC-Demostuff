from celery import Celery
import time
from hookClient import Client
import send_email

app = Celery('celery_app', broker='redis://localhost:6379/1',backend="rpc://")

@app.task
def delay_one_min(username):
    print("Executing delay_one_min")
    emailid =""
    client = Client()
    emailid = ""
    time.sleep(60)
    print("sleep over")
    emailid = client.get_hook(username)
    print("in job",emailid)
    message = "Job Completed.\nYou are recieving this notification because you have subscribed to callback @ gRPC-Demo"
    send_email.email(emailid,message)
    print("Job completed")


