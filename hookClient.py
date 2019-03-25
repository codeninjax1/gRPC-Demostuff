import grpc
import hook_pb2
import hook_pb2_grpc

class Client(object):
    def __init__(self):
        self.port = 50051
        self.channel = grpc.insecure_channel("127.0.0.1:{}".format(self.port))
        self.stub = hook_pb2_grpc.webHookStub(self.channel)

    def create(self,name,link):
        message = {"username":name,"link":link}
        data = hook_pb2.User(**message)
        result = self.stub.hookCreate(data)
        print(result)

c = Client()
c.create("harish","http://test")

