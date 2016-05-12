import feedparser

TC_NEWS_FEED_URL = "http://techcrunch.com/feed/"
TNW_NEWS_FEED_URL = "http://thenextweb.com/feed/"

SUBSCRIBE_CATEGORY = ['mobile', 'developer', 'entrepreneur', 'tech', 'apps', 'startups', 'startup', 'software engineering']

class NewsFeed(object):
    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description
        
    def __str__(self):
        return u"Title: {title}\nURL: {url}\n".format(title=self.title, url=self.link).encode('utf-8')   
    

def read_subscribe_news_feed(url):
    def has_subscribe_category(post):
        for tag in post.get('tags'):
            if tag['term'].lower() in SUBSCRIBE_CATEGORY:
                return True
        return False             
    
    feed = feedparser.parse(url)
    for post in feed.entries:
          if has_subscribe_category(post):
              yield NewsFeed(post.title, post.link, post.description)
                     
        
if __name__ == '__main__':
    for tnw_news in read_subscribe_news_feed(TNW_NEWS_FEED_URL):
        print tnw_news
    for tc_news in read_subscribe_news_feed(TC_NEWS_FEED_URL):
        print tc_news
    