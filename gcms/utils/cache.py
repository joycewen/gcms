# coding: utf-8

import functools
import operator

import redis

from gcms.utils import config


host = config.get('redis', 'host')
port = config.get('redis', 'port')
db = config.get('redis', 'db')
redis_server = redis.StrictRedis(host, port)


class CacheManager(object):
    def __init__(self):
        self.cache = redis_server

    def delete(self, *names):
        return self.cache.delete(*names)

    # key -> value
    def get_by_key(self, key):
        return self.cache.get(key)

    # key* -> [key1, key2, key3]
    def get_keys(self, pattern):
        return self.cache.keys(pattern)

    # key ->list -> list[start:end]
    def get_sort_list(self, key, start, end):
        return self.cache.zrange(key, start, end)

    # [get_by_key(refix + key) for key in keys]
    def get_by_keys(self, prefix, keys):
        properties = self.cache.mget(map(functools.partial(operator.add, prefix), keys))

        return dict(zip(keys, properties))

    def exists_key(self, name):
        return self.cache.exists(name)

    def exists(self, key, value):
        return self.cache.zscore(key, value)

    def zrange(self, name, start, stop):
        return self.cache.zrange(name, start, stop)

    def zrangebyscore(self, name, min, max, start=None, num=None, withscores=False):
        return self.cache.zrangebyscore(name, min, max, start, num, withscores)

    def zrevrange(self, name, start, stop):
        return self.cache.zrevrange(name, start, stop)

    def zrevrangebyscore(self, name, score, count):
        return self.cache.zrevrangebyscore(name, score, '-inf', start=0, num=count)

    def smembers(self, name):
        return self.cache.smembers(name)

    def index(self, name, key):
        return self.cache.zrank(name, key)

    def set(self, name, value, expire=None):
        if expire:
            self.cache.set(name, value)
            self.cache.expire(name, expire)
        else:
            self.cache.set(name, value)

    def zcount(self, name, min, max):
        return self.cache.zcount(name, min, max)

    def zcard(self, name):
        return self.cache.zcard(name)

    def get_next_id(self, key):
        return self.cache.incr(key)

    def incr(self, key):
        return self.cache.incr(key)

    def get(self, key):
        return self.cache.get(key)

    def mget(self, keys, *args):
        return self.cache.mget(keys, *args)

    def sismember(self, key, member):
        return self.cache.sismember(key, member)

    def __getitem__(self, item):
        return self.cache.get(item)
