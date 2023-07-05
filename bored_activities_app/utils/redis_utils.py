import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

class RedisUtil:

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        self.client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    def set_value(self,key,value):
        self.client.set(key, value,keepttl=3600)
        return True

    def get(self,key):
        return self.client.get(key)
