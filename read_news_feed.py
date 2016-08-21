import multiprocessing
import time
import operator
from read_config import read_feed_config
from news_feed import read_subscribe_news_feed
from common import const
from common.utils import unpack_args
from db_manager import get_value     
    
            
def read_config_all_subscribe_news_feed():
    config = read_feed_config()
    return get_news_feed(config[const.FEED_URL], config[const.CATEGORY])
    

def read_config_all_subscribe_news_feed_in_parallel():
    config = read_feed_config()
    return get_news_feed_in_parallel(config[const.FEED_URL], config[const.CATEGORY])    
    
            
def read_db_all_subscribe_news_feed():
    urls = get_value(const.FEED_URL)
    categories = get_value(const.CATEGORY)
    for url in urls:
        for news in read_subscribe_news_feed(url, categories):
            yield news  
            
            
def read_db_all_subscribe_news_feed_in_parallel():
    urls = get_value(const.FEED_URL)
    categories = get_value(const.CATEGORY)
    return get_news_feed_in_parallel(urls, categories)
                    

def get_news_feed(urls, categories):
    news_list = []
    for url in urls:
        news_list.extend([news for news in read_subscribe_news_feed(url, categories)])
    return news_list
                            
                        
def get_news_feed_in_parallel(urls, categories):
    pool_size = multiprocessing.cpu_count() * 2
    process_pool = multiprocessing.Pool(processes=pool_size)
    news_list = process_pool.map(read_subscribe_news_feed_wrapper, [(url, categories) for url in urls])
    return reduce(operator.add, news_list)
    
    
@unpack_args    
def read_subscribe_news_feed_wrapper(url, categories):
    return list(read_subscribe_news_feed(url, categories))
        
    
if __name__ == '__main__':
    start_time = time.time()
    news_list = read_config_all_subscribe_news_feed()
    end_time = time.time()
    print "Running read_config_all_subscribe_news_feed() in {} seconds".format(end_time-start_time)
    start_time = time.time()
    news_list = read_config_all_subscribe_news_feed_in_parallel()
    end_time = time.time()
    print "Running read_config_all_subscribe_news_feed_in_parallel() in {} seconds".format(end_time-start_time)


