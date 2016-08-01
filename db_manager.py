import redis

app_redis = redis.StrictRedis(host='localhost',port= 6379)


def get_value(key):
    return app_redis.get(key)
    
    
def set_value(key, value):
    app_redis.set(key, value)
    
    
def add_to_list(key, value):
    app_redis.lpush(key, value)
    
    
def get_list(key):
    return app_redis.lrange(key, 0, -1)

