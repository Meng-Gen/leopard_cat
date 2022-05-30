"""Module to crawl feed sources."""

import logging

from leopard_cat.crawler.feed_source import FeedSource


class Crawler():
  """Class for crawling feed sources."""

  def crawl(self, feed_source: FeedSource, output_filepath: str) -> None:
    """Crawls the feed source.

    Args:
      feed_source: The feed source to be crawled.
      output_filepath: The output file path on the host.
    """
    logging.debug('Crawling %r feed source to %s on the host',
                  feed_source, output_filepath)
