import os
import feedparser
from time import mktime
from datetime import datetime


class NewsFeed(object):
    def __init__(self, title, link, description, published_date):
        self.title = title
        self.link = link
        self.description = description
        self.published_date = published_date
        
    def __str__(self):
        return u"Title: {title}\nURL: {url}\nDescription: {desc}".format(title=self.title, url=self.link, desc=self.description).encode('utf-8')   
    

def read_subscribe_news_feed(url, subscribe_category):    
    def has_subscribe_category(post):
        for tag in post.get('tags'):
            if tag['term'].lower() in subscribe_category:
                return True
        return False             
    
    feed = feedparser.parse(url)
    for post in feed.entries:
          if has_subscribe_category(post):
              yield NewsFeed(post.title, post.link, post.description, datetime.fromtimestamp(mktime(post.published_parsed)))

