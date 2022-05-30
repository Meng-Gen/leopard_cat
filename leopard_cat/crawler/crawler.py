"""Module to crawl feed sources."""

from leopard_cat.crawler.feed_source import FeedSource


class Crawler():
  """Class for crawling feed sources."""

  def crawl(self, feed_source: FeedSource) -> None:
    """Crawls the feed source.

    Args:
      feed_source: The feed source to be crawled.
    """
    print(feed_source)
