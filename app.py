from flask import Flask, jsonify, render_template
from cache import get_cached_data, set_cache_data, clear_cache, test_redis
from data_source import fetch_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')  


@app.route("/test-redis")
def check_redis():
    return test_redis()


@app.route("/data")
def get_data():
    cache_key = "my_data"
    cached = get_cached_data(cache_key)
    if cached:
        return jsonify({"source": "cache", "data": cached})

    data = fetch_data()
    set_cache_data(cache_key, data, ttl=30)  # TTL = 30 seconds
    return jsonify({"source": "database", "data": data})

@app.route("/clear-cache")
def clear():
    clear_cache()
    return jsonify({"message": "Cache cleared!"})

if __name__ == "__main__":
    app.run(debug=True)
