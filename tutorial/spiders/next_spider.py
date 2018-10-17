import scrapy
import hashlib

def mhash(s):
    return int(hashlib.md5(s).hexdigest()[:8], 16)

class NextSpider(scrapy.Spider):
    name = "next"
    start_urls = [
        'https://www.pro-football-reference.com/years/2018/games.htm',
    ]




    def parse(self, response):
        week = 1
        pweek = 0
        for rows in  response.xpath('//table[@id="games"]//tbody//tr'):
            #If it's a separator between weeks, use that to update the week
            valid_row =  rows.xpath('td[1]//text()').extract(),
            if len(valid_row[0]) == 0:
                week += 1
                continue

            #if it's the end of the season so far (last week played) stop.
            end_played_so_far=  rows.xpath('td[8]//text()').extract(),
            if len(end_played_so_far[0]) != 0:
                continue

            if pweek == 0:
                pweek = week

            if pweek != week:
                break

            yield{
                'week': week,
                'day': mhash(rows.xpath('td[1]//text()').extract()[0]),
                'date': mhash(rows.xpath('td[2]//text()').extract()[0]),
                'time': mhash(rows.xpath('td[3]//text()').extract()[0]),
                'winner': mhash(rows.xpath('td[4]//text()').extract()[0]),
                #'winner_home': rows.xpath('td[5]//text()').extract(),
                'loser': mhash(rows.xpath('td[6]//text()').extract()[0]),
                'ptstot': 0,
            }

