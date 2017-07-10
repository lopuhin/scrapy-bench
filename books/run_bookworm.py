from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings
from twisted.internet import reactor, defer

from books.spiders.followall import FollowAllSpider
import books.settings


settings = Settings()
settings.setmodule(books.settings)

configure_logging()
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    for _ in range(5):
        yield runner.crawl(FollowAllSpider)
    reactor.stop()

crawl()
reactor.run()
