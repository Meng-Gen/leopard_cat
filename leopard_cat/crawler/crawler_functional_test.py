"""Functional tests for crawler."""

import unittest

from leopard_cat.crawler.crawler import Crawler
from leopard_cat.crawler.url_source import UrlSource


class CrawlerFunctionalTest(unittest.TestCase):
  """Functional tests for Crawler class."""

  def test_crawl(self):
    """Tests for crawling."""
    crawler = Crawler()
    source = UrlSource(
        name='web_resource/twse/mops/operating_income/2021/01',
        link='https://mops.twse.com.tw/nas/t21/sii/t21sc03_110_1.csv')
    crawler.crawl(source=source)
