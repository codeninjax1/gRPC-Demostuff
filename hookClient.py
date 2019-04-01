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

    def get_hook(self,name):
        message = {"username":name}
        data = hook_pb2.Hook(**message)
        result = self.stub.hookGet(data)
        output = result.response
        print("in client hook function")
        print(output)
        return output

if __name__ == "__main__":
    c = Client()
    c.create("harish","http://test")
    c.get_hook("harish")

