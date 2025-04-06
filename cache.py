import redis
import json

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def test_redis():
    try:
        r.set("test", "Redis is working!")
        return r.get("test")
    except Exception as e:
        return str(e)


def get_cached_data(key):
    value = r.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache_data(key, data, ttl=60):
    r.setex(key, ttl, json.dumps(data))

def clear_cache():
    r.flushdb()

