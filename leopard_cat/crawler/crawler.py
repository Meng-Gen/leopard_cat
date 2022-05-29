"""Module to crawl feed sources."""

from leopard_cat.crawler.feed_source import FeedSource


class Crawler():
  """Class for crawling feed sources."""

  def crawl(self, feed_source: FeedSource) -> None:
    """Crawls the feed source."""
    print(feed_source)
    pass
