import os
import redis
from flask import Flask, render_template, url_for, request, redirect
from read_news_feed import (
    read_config_all_subscribe_news_feed_in_parallel, 
    read_db_all_subscribe_news_feed_in_parallel
)
from common import const   
from db_manager import add_to_list, get_list, set_value, get_value
from werkzeug.contrib.fixers import ProxyFix
       

app = Flask(__name__)


@app.route("/")
def main():
    news_list = sorted(read_config_all_subscribe_news_feed_in_parallel(), key=lambda x:x.published_date, reverse=True)
    return render_template('index.html', news_list=news_list)
    
    
@app.route("/list")
def feeds():
    news_list = sorted(read_db_all_subscribe_news_feed_in_parallel(), key=lambda x:x.published_date, reverse=True)
    return render_template('index.html', news_list=news_list) 
    
    
@app.route("/add_category/<category>")
def add_category(category):   
    add_to_list(const.CATEGORY, category)
    return 'Category {} is added'.format(category)
    

@app.route("/view_category")
def view_category():   
    categories = get_list(const.CATEGORY)
    return 'Categories: {}'.format(",".join(categories))
    
    
@app.route("/set_token")
def set_token():
    return render_template('token_form.html')
    

@app.route("/update_token/", methods=['POST'])    
def update_token():
    set_value('token', request.form['token']);
    return redirect(url_for('main'))
    
    
app.wsgi_app = ProxyFix(app.wsgi_app)            

if __name__ == "__main__":
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, threaded=True)
    
