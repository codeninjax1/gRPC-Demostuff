import falcon
import json
from client import Client

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

app = falcon.API()

user_create = UserCreate()
user_auth = UserAuth()
app.add_route("/register",user_create)
app.add_route("/auth",user_auth)
