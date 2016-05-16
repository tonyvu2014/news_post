import feedparser
from read_config import read_config

class NewsFeed(object):
    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description
        
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
              yield NewsFeed(post.title, post.link, post.description)
              
            
def read_all_subscribe_news_feed(feed_file):              
    config = read_config(feed_file)
    for url in config['feed_url']:
        for news in read_subscribe_news_feed(url, config['category']):
            yield news               
        
        
if __name__ == '__main__':
    for news in read_all_subscribe_news_feed('feed_config.json'):
        print news

