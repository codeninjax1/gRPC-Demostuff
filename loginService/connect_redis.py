import redis
import json

class connectRedis:

    # Set Host and Port to connect to redis server
    def __init__(self,host,port):
        self.host = "127.0.0.1"
        self.port = 6379
        self.redis_client = redis.StrictRedis(host=self.host,port=self.port,decode_responses=True)

    # Save username and password to redis
    def saveUser(self,username,token,key):

        #Optimize the iteration
        # Check if user already exist
        keys = self.redis_client.keys()
        for key in keys:
            data = self.redis_client.get(key)
            data = json.loads(data)
            if type(data) is dict and "username" in data.keys() and data["username"]==username:
                print("delete this entry")
                print(data)
                self.redis_client.delete(key)
        try:
            values = json.dumps({"username":username,"key":key})
            result = self.redis_client.set(token,values)
            return token
        except Exception as e:
            print(e)
            return {}

    # Retrieve password of the user
    def getPassword(self,username):
        try:
            result = self.redis_client.get(username)
            print("get passwd",result)
            if result == "":
                print("User Does not exist")
                return ""
            return result
        except Exception as e:
            print(e)
            return ""

    def authenticate_token(self,token):
        try:
            result = self.redis_client.get(token)
            if result == None:
                print("Token does not exist")
                return ""
            return result
        except Exception as e:
            print(e)
            return ""


