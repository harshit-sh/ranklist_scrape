# acm spider

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from codechef_scrape.items import CodechefScrapeItem

class ACMSpider(BaseSpider):
    name = "acm"
    allowed_domains = ["codechef.com"]
    CONCURRENT_REQUESTS = 1
    start_urls = [
       "http://www.codechef.com/teams/list/ACMAMR14?page=%d" % i for i in xrange(1,63)
      ]
    download_delay = 5

    def parse(self, response):
    	hxs = Selector(response)
    	table = hxs.xpath('//table[@class="rank-table"]')

    	ranks = table.xpath('.//td/b/text()').extract()


    	teams_temp = table.xpath('.//td/a/text()').extract()
    	teams_temp = [x for x in teams_temp if x != 'acmicpcuser']
    	team_names = teams_temp

    	institutions_temp = table.xpath('.//td/text()').extract()[7:]
    	institutions_temp = [x for x in institutions_temp if x != ', ']
    	institutions = institutions_temp[::2]
    	scores = institutions_temp[1::2]
    	final = zip(ranks,team_names,scores,institutions)

    	for i in final:
 			item = CodechefScrapeItem()
	   		item['rank'] = i[0]
			item['team_name'] = i[1]
			item['institution'] = i[3]
			item['score'] = i[2]
			yield item



