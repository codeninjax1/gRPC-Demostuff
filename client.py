import json
import user_pb2
import user_pb2_grpc
import grpc

class Client(object):
    def __init__(self):
        self.port = 8005
        self.channel = grpc.insecure_channel("127.0.0.1:{}".format(self.port))      
        self.stub = user_pb2_grpc.userLoginStub(self.channel)

    def register(self,name,password):
        
        message = {"username":name,"password":password}
        data = user_pb2.User(**message)
        result = self.stub.userCreate(data)
        print("in register")
        print(result.response)
        return result.response

    def authenticate(self,name,password):

        message = {"username":name,"password":password}
        data = user_pb2.User(**message)
        result = self.stub.userAuth(data)
        print(result)
        print("auth")
        return result.response

    def authenticate_token(self,token):

        message = {"token":token}
        print(token)
        data = user_pb2.Token(**message)
        result = self.stub.tokenAuth(data)
        print("in client")
        print(result.response)
        return result.response

#client = Client()
#client.register("harish","test1")
#client.authenticate("harish","test")
