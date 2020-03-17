import redis
from setting import ConfigService

object = ConfigService

log = object.logger


class RedisService:

    def __init__(self):
        self.connect = self.connection()

    def connection(self):
        try:
            conn = redis.Redis(**object.CACHE)
            log.info("===========> cache is connected: {}".format(conn))
            return conn
        except:
            return "connection failed"

    def set_key(self, key, value):
        self.connect.set(key, value)
        print("set key and value")

    def get_value(self, key):
        value = self.connect.get(key)
        return value

    def delete(self, key):
        self.connect.delete(key)
        return "delete key"

    def set_dict_key(self, dict_key, dict):
        print("true")
        self.connect.hmset(dict_key, dict)
        print("hset")
        return "set dict"

    def get_dict_value(self, key):
        data = self.connect.hgetall(key)
        return data
