"""Functional tests for crawler."""

import unittest

from leopard_cat.crawler.crawler import Crawler
from leopard_cat.crawler.feed_source import FeedSource


class CrawlerFunctionalTest(unittest.TestCase):
  """Functional tests for Crawler class."""

  def test_crawl(self):
    """Tests for crawling."""
    crawler = Crawler()
    feed_source = FeedSource(
        name='web_resource/twse/mops/operating_income/2021/01',
        url_link='https://mops.twse.com.tw/nas/t21/sii/t21sc03_110_1.csv')
    crawler.crawl(feed_source=feed_source)
