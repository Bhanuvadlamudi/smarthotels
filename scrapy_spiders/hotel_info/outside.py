from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json
import numpy as np
import pandas as pd

with open('/Users/argha/Desktop/cityhotels/CaliforniaState_hotels.json') as f:
    data = [json.loads(line) for line in f]
Urls = [u for u in pd.DataFrame(data)['HotelUrl']]
Urls = np.reshape(Urls,len(Urls))

process = CrawlerProcess(get_project_settings())
process.crawl('hotel_details', domain='booking.com', start_urls = Urls)
process.start()
