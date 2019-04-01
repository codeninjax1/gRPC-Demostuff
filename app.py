import falcon
import json
from client import Client
import hookClient
from celery_app import delay_one_min

class UserCreate(object):
    def __init__(self):
        self.conn = Client()

    def on_post(self,req,resp):
        data = req.stream.read()
        data = json.loads(data)
        username = data["username"]
        password = data["password"]
        self.conn.register(username,password)
        #self.conn.authenticate(username,password)

class UserAuth(object):
    def __init__(self):
        self.conn = Client()

    def on_post(self,req,resp):
        data =req.stream.read()
        data =json.loads(data)
        username = data["username"]
        password = data["password"]
        result = self.conn.authenticate(username,password)

        if result == True:
            resp.body = json.dumps({"result":"Auth Success","status":"success"})
            return
        else:
            resp.body = json.dumps({"result":"Auth Failed","status":"failed"})
            return

class Hook(object):
    def __init__(self):
        self.client = hookClient.Client()
    def on_post(self,req,resp):
        print("in hook client")
        data =req.stream.read()
        data =json.loads(data)
        username = data["username"]
        callback = data["callback"]
        print("save hook")
        self.client.create(username,callback)
        print("before running the job")
        random_job = delay_one_min.delay(username)
        print("Job is initiated")
        # code to save the hook
        resp.body = json.dumps({"result":"callback registered. You'll recieive it once the random job is completed","status":"success"})

app = falcon.API()

user_create = UserCreate()
user_auth = UserAuth()
user_callback = Hook()
app.add_route("/register",user_create)
app.add_route("/auth",user_auth)
app.add_route("/longjob",user_callback)
