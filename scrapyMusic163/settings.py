# -*- coding: utf-8 -*-

# Scrapy settings for scrapyMusic163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import urllib

BOT_NAME = 'scrapyMusic163'

SPIDER_MODULES = ['scrapyMusic163.spiders']
NEWSPIDER_MODULE = 'scrapyMusic163.spiders'


#mongo


# ITEM_PIPELINES = {
#     "scrapyMusic163.pipelines.MongoPipeline":900
# }
#
# MONGO_URI = 'mongodb://root:'+urllib.parse.quote('MyNewPass+@321')+'@localhost:27017'
# MONGO_DATABASE = 'scrapy'
# MONGO_DB = 'taobao'

ITEM_PIPELINES = {
  "scrapy_mongodb.MongoDBPipeline":900
}

MONGODB_URI = 'mongodb://root:'+urllib.parse.quote('MyNewPass+@321')+'@localhost:27017'
MONGODB_DATABASE = 'scrapy'
# MONGODB_COLLECTION = 'my_items'
MONGODB_UNIQUE_KEY = 'realLink'

MONGODB_SEPARATE_COLLECTIONS = True

# 编码
FEED_EXPORT_ENCODING = 'utf-8'

#SPLASH SERVER
SPLASH_URL = 'http://127.0.0.1:8050/render.json'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}


SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapyMusic163 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

MAX_PAGE = 100
SPLASH_COOKIES_DEBUG= True
# COOKIES_DEBUG= True
# DUPEFILTER_DEBUG =True

# DOWNLOADER_MIDDLEWARES = {
#     scrapy.downloadermiddlewares.cookies.CookiesMiddleware
# }

# COOKIES_ENABLED=true

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Cookie':'_iuqxldmzr_=32; _ntes_nnid=675672128402b92fb6fff067f817430b,1524885386164; _ntes_nuid=675672128402b92fb6fff067f817430b; __utmz=94650624.1524885389.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); WM_TID=ap2Bbk2JNjl9HMBjNVNPYZTCl5rKHrkT; JSESSIONID-WYYY=EMba6PicaoqybOfHF%2F%2FQq0n1f%5C9rsMuAj3AHhUUz3N6kAwnFIqnEDJPFcrvkqf17VB0h21Sa225CTzdf%5C9VJC5yBxupIwNX5dwmD5gWMgEf%2BF7Cm44QEEo4lhb3%2B%5CbDjhC0o%5CmFZ4fpf1zkqzwHv7Bnf8NSEIJ6Vm7NV6Qiv0OTNCjk%5C%3A1525231076766; __utma=94650624.1499405674.1524885387.1524896358.1525229277.5; __utmc=94650624; __utmb=94650624.10.10.1525229277',
#     # 'DNT': '1',
#     'Host': 'music.163.com',
#     'Pragma': 'no-cache',
#     'Referer': 'http://music.163.com/',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# }


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapyMusic163.middlewares.Scrapymusic163SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapyMusic163.middlewares.Scrapymusic163DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrapyMusic163.pipelines.Scrapymusic163Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
