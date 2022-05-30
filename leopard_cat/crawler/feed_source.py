"""Module to define feed source data structure."""

import collections


FeedSource = collections.namedtuple('FeedSource', ('name', 'url_link'))
