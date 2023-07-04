import redis
from .utils import *


redis_host = "localhost"
redis_port = 6379
redis_password = ""




def key():
    secret_key = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    key = random_string_generator(32)
    secret_key.set("redis_key:key", key)
    redis_key = secret_key.get("redis_key:key")
    return redis_key