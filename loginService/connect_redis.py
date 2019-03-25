import redis

class connectRedis:

    # Set Host and Port to connect to redis server
    def __init__(self,host,port):
        self.host = "127.0.0.1"
        self.port = 6379
        self.redis_client = redis.StrictRedis(host=self.host,port=self.port,decode_responses=True)

    # Save username and password to redis
    def saveUser(self,username,password):
        try:
            result = self.redis_client.set(username,password)
            return result
        except Exception as e:
            print(e)
            return False

    # Retrieve password of the user
    def getPassword(self,username):
        try:
            result = self.redis_client.get(username)
            if result == "":
                print("User Does not exist")
                return ""
            return result
        except Exception as e:
            print(e)
            return ""


