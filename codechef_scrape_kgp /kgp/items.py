# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CodechefScrapeItem(Item):
    # define the fields for your item here like:
    rank = Field()
    team_name = Field()
    score = Field()
    institution = Field()
