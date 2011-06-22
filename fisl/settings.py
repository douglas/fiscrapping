# Scrapy settings for fisl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'fisl'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['fisl.spiders']
NEWSPIDER_MODULE = 'fisl.spiders'
DEFAULT_ITEM_CLASS = 'fisl.items.FislItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
