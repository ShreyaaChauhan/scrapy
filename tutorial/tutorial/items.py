# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

# from dataclasses import dataclass, field
from typing import Optional


class TutorialItem(Item):
    # define the fields for your item here like:
    name = Field()
    title = Field()
    image = Field()
    price = Field()
    stock = Field()
    stars = Field()
    description = Field()
    upc = Field()
    price_after_tax = Field()
    price_incl_tax = Field()
    tax = Field()


# @dataclass
# class TutorialItem:
#     title: Optional[str] = field(default=None)
#     image: Optional[str] = field(default=None)
#     price: Optional[str] = field(default=None)
#     stock: Optional[str] = field(default=None)
#     stars: Optional[str] = field(default=None)
#     description: Optional[str] = field(default=None)
#     upc: Optional[str] = field(default=None)
#     price_after_tax: Optional[str] = field(default=None)
#     price_incl_tax: Optional[str] = field(default=None)
#     tax: Optional[str] = field(default=None)
