import requests
import json
import random
import schedule
import time
import os
from read_news_feed import NewsFeed, read_all_subscribe_news_feed
from read_config import read_config
from common.time_frame import TimeFrame
from common import const


LINKEDIN_URL="https://www.linkedin.com"
SHARE_API_URL = "https://api.linkedin.com/v1/people/~/shares?format=json"

    
def share_on_linkedin(newsfeed):
    payload = {
        "content": {
            "title": newsfeed.title,
            "submitted-url": newsfeed.link,  
        },
        "visibility": {
            "code": "anyone"
        }  
    }
    api_file = os.path.dirname(os.path.realpath(__file__)) + "/json/api_config.json"
    config = read_config('json/api_config.json')
    headers = {'content-type': 'application/json', 'x-li-format': 'json', 'Authorization': 'Bearer {}'.format(config[const.CODE])}
    print u"Sharing: {}".format(newsfeed.title).encode('utf-8')
    r = requests.post(SHARE_API_URL, data = json.dumps(payload), headers=headers)
    print r.json()

    
def share_random():
    feed_file = os.path.dirname(os.path.realpath(__file__)) + "/json/feed_config.json"
    news_list = list(read_all_subscribe_news_feed(feed_file))
    news = random.choice(news_list)
    share_on_linkedin(news)
    
    
def share_all():
    feed_file = os.path.dirname(os.path.realpath(__file__)) + "/json/feed_config.json"
    for news in read_all_subscribe_news_feed(feed_file):
        share_on_linkedin(news)
        
        
def schedule_share(time_frame, time_point=None):
    if time_frame == TimeFrame.Minute:
        job = schedule.every(time_point).minute.do(share_random) if time_point else schedule.every().minute.do(share_random)
    elif time_frame == TimeFrame.Hour:    
        job = schedule.every().hour.at(time_point).do(share_random) if time_point else schedule.every().hour.do(share_random)
    elif time_frame == TimeFrame.Day:
        job = schedule.every().day.at(time_point).do(share_random) if time_point else schedule.every().day.do(share_random)
    elif time_frame == TimeFrame.Week:    
        job = schedule.every().monday.do(share_random)
    else:
        pass
    if job:
        while True:
            schedule.run_pending()
            time.sleep(5)
          
          
if __name__ == '__main__':
    share_all()
   
