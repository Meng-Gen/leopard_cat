"""Module to crawl feed sources."""

import logging

from leopard_cat.crawler.feed_source import FeedSource


class Crawler():
  """Class for crawling feed sources."""

  def crawl(self, feed_source: FeedSource) -> None:
    """Crawls the feed source.

    Args:
      feed_source: The feed source to be crawled.
    """
    logging.debug('Crawling %r feed source', feed_source)
