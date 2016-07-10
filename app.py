import os
import redis
from flask import Flask, render_template
from src.read_news_feed import read_all_subscribe_news_feed

app = Flask(__name__)
app.redis_server = redis.StrictRedis(host='localhost',port= 6379)


@app.route("/")
def main():
    news_list = read_all_subscribe_news_feed('src/json/feed_config.json')
    return render_template('index.html', news_list=news_list)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)