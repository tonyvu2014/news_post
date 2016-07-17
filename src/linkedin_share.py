import requests
import json
import random
import schedule
import time
import os
from read_news_feed import NewsFeed, read_all_subscribe_news_feed
from read_config import read_api_config
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
    config = read_api_config()
    headers = {'content-type': 'application/json', 'x-li-format': 'json', 'Authorization': 'Bearer {}'.format(config[const.CODE])}
    print u"Sharing: {}".format(newsfeed.title).encode('utf-8')
    r = requests.post(SHARE_API_URL, data = json.dumps(payload), headers=headers)
    print r.json()

    
def share_random():
    news_list = list(read_all_subscribe_news_feed())
    news = random.choice(news_list)
    share_on_linkedin(news)
    
    
def share_all():
    for news in read_all_subscribe_news_feed():
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
   
