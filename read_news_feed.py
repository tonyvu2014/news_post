from read_config import read_feed_config
from news_feed import read_subscribe_news_feed
from common import const
from db_manager import get_value            
    
            
def read_config_all_subscribe_news_feed():
    config = read_feed_config()
    for url in config[const.FEED_URL]:
        for news in read_subscribe_news_feed(url, config[const.CATEGORY]):
            yield news
    
            
def read_db_all_subscribe_news_feed():
    urls = get_value(const.FEED_URL)
    print "URLs: {}".format(str(urls))
    categories = get_value(const.CATEGORY)
    print "Categories: {}".format(str(categories))
    for url in urls:
        for news in read_subscribe_news_feed(url, categories):
            yield news   
                        
    
if __name__ == '__main__':
    for news in sorted(list(read_config_all_subscribe_news_feed()), key=lambda x: x.published_date, reverse=True):
        print news
        print "\n"



