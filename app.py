import os
import redis
import validators
from flask import Flask, render_template, url_for, request, redirect
from read_news_feed import (
    read_config_all_subscribe_news_feed_in_parallel, 
    read_db_all_subscribe_news_feed_in_parallel
)
from common import const   
from db_manager import add_to_list, get_list, set_value, get_value, del_key
from werkzeug.contrib.fixers import ProxyFix
       

app = Flask(__name__)


@app.route("/")
def main():
    news_list = sorted(read_db_all_subscribe_news_feed_in_parallel(), key=lambda x:x.published_date, reverse=True)
    return render_template('index.html', news_list=news_list)
    
    
# @app.route("/list")
# def feeds():
#     news_list = sorted(read_db_all_subscribe_news_feed_in_parallel(), key=lambda x:x.published_date, reverse=True)
#     return render_template('index.html', news_list=news_list)
    
    
@app.route("/update_category/", methods=["POST"])
def update_category():
    category = request.form[const.CATEGORY].split(",")  
    del_key(const.CATEGORY)
    add_to_list(const.CATEGORY, category)
    return redirect(url_for('main'))
    

@app.route("/set_category")
def set_category():   
    categories = get_list(const.CATEGORY)
    category_value = ",".join(categories)
    return render_template('category_form.html', category_value=category_value)
    
    
@app.route("/set_token")
def set_token():
    client_id_value = get_value(const.CLIENT_ID)
    client_secret_value = get_value(const.CLIENT_SECRET)
    redirect_uri_value = get_value(const.REDIRECT_URI)
    code_value = get_value(const.CODE)
    tokens = {
        const.CLIENT_ID: client_id_value,
        const.CLIENT_SECRET: client_secret_value,
        const.REDIRECT_URI: redirect_uri_value,
        const.CODE: code_value
    }    
    print(str(tokens))
    return render_template('token_form.html', tokens=tokens)
    

@app.route("/update_token/", methods=['POST'])    
def update_token():
    set_value(const.CLIENT_ID, request.form[const.CLIENT_ID])
    set_value(const.CLIENT_SECRET, request.form[const.CLIENT_SECRET])
    set_value(const.CODE, request.form[const.CODE])
    set_value(const.REDIRECT_URI, request.form[const.REDIRECT_URI])
    return redirect(url_for('main'))
    
    
@app.route("/set_feed")    
def set_feed():
    feeds = get_list(const.FEED)
    return render_template('feed_form.html', feeds=feeds)
  
    
@app.route("/update_feed/", methods=["POST"])
def update_feed():
    feed = filter(lambda x: validators.url(x), request.form.getlist(const.FEED))
    del_key(const.FEED)
    add_to_list(const.FEED, feed)
    return redirect(url_for('main'))
        
    
app.wsgi_app = ProxyFix(app.wsgi_app)            


if __name__ == "__main__":
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, threaded=True)
    
