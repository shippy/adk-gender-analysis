# 1. Download the list of all debaters; identify gender according to the list of names.
# 2. Use Scrapy to go through all the debates; save Debater.id / Debate.id / speakerpoints
# 	association, as well as Debate / Tournament / Competition / Language assoc.
# (See MySQL starter: http://www.mikusa.com/python-mysql-docs/index.html)
# (See peewee)
# 3. Use matplotlib to do the math? Or export the data to R to make pretty graphs?
"""
import mysqldb as mq

db = mq.connect(host = 'localhost', user = 'data', passwd = '', db = 'data')
cur = db.cursor()

import peewee
from peewee import *

db = MySQLDatabase('jonhydb', user='john',passwd='megajonhy')

class Debater(peewee.Model):
	author = peewee.CharField()
	title = peewee.TextField()

class Meta:
	database = db

Book.create_table()
book = Book(author="me", title='Peewee is cool')
book.save()

for book in Book.filter(author="me"):
	print book.title
"""

# For starters, scrape one debate... or scrape one person? Maybe that's easier.
from scrapy.item import Item, Field

class Debater(Item):
	ident = Field()
	name = Field()
	gender = Field()
	points = Field()
	
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class MininovaSpider(CrawlSpider):
    name = 'debater'
    allowed_domains = ['debatovani.cz']
    start_urls = ['http://debatovani.cz/greybox/?page=lide&kdo=debateri']
    rules = [Rule(SgmlLinkExtractor(allow=['./?page=clovek&amp;clovek_id=\d+']), 'parse_debater')]

    def parse_debater(self, response):
        sel = Selector(response)
        person = Debater()
        person['ident'] = response.url
        #person['name'] = sel.xpath("//h1/text()").extract()
        #person['gender'] = 
        #person['points'] = sel.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
        return person



