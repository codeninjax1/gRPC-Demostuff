import grpc
import user_pb2
import user_pb2_grpc
import time
from concurrent import futures
from token_management import new_token
from connect_redis import connectRedis
import json

class userLoginService(user_pb2_grpc.userLoginServicer):
    
    def __init__(self):
        self.server_port = 8005
        self.redis = connectRedis(host="127.0.0.1",port=6479)

    def userCreate(self,request,context):
        name = request.username
        password = request.password
        print(name)
        print(password)
        token = new_token(name,password)       
        result = self.redis.saveUser(name,token["token"],token["hash"]).decode("utf-8")
        print(result)
        result_success = {"response":result}
        result_fail = {"response":"failed"}

        if result != {}:
            return user_pb2.Response(**result_success)
        else:
            return user_pb2.Response(**result_fail) 

       # return user_pb2.Response(**result)

    def userAuth(self,request,context):
        name = request.username
        password = request.password
        print(name)
        print(password)
        auth_success = {"response":True}
        auth_fail = {"response":False}

        result = self.redis.getPassword(name)
        print("auth response",result==password)
        if password==result:
            return user_pb2.Response(**auth_success)
        elif result=="":
            return user_pb2.Response(**auth_fail)
        else:
            return user_pb2.Response(**auth_fail)
    
    def run(self):
        grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        user_pb2_grpc.add_userLoginServicer_to_server(userLoginService(),grpc_server)
        grpc_server.add_insecure_port('127.0.0.1:{}'.format(self.server_port))
        grpc_server.start()

        try:
            while True:
                time.sleep(60000)

        except KeyboardInterrupt:
            grpc_server.stop(0)
            print("Stopped")


server = userLoginService()
server.run()

