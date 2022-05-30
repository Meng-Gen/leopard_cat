"""Module to crawl URL sources."""

from leopard_cat.crawler.url_source import UrlSource


class Crawler():
  """Class for crawling feed sources."""

  def crawl(self, source: UrlSource) -> None:
    """Crawls the URL source.

    Args:
      source: The URL source to be crawled.
    """
    print(source)
    pass
