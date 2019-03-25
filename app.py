import falcon
import json
from client import Client

class HelloWorld():
    def __init__(self):
        self.conn = Client()

    def on_get(self,req,resp):
        resp.body = json.dumps("Hello World")
        self.conn.register("test1","test1")
        self.conn.authenticate("test1","test1")

app = falcon.API()

hello = HelloWorld()

app.add_route("/test",hello)

