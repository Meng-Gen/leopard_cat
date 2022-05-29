"""Functional tests for crawler."""

import unittest

from leopard_cat.crawler.crawler import Crawler

class CrawlerFunctionalTest(unittest.TestCase):
  """Functional tests for Crawler class."""

  def test_crawl(self):
    """Tests for crawling."""
    crawler = Crawler()
    crawler.crawl()
