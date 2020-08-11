import scrapy
import json


class HamroPatroSpider(scrapy.Spider):
    name = "hamro_patro"

    new_data = []
    year = 2077
    months = []
    for i in range(1, 13):
        months.append(i)
    start_urls = []
    for month in months:
        start_urls.append(
            "https://www.hamropatro.com/calendar/{}/{}/".format(year, month))

    def parse(self, response):
        data = []
        res = response.css('.calendar .dates li:not([class^="disable"])')
        month = response.url.split("/")[-1]
        for r in res:
            mydict = {
                'tithi': r.css('span.tithi::text').get().encode('utf-8'),
                'event': r.css('span.event::text').get().encode('utf-8'),
                'day': r.css('span.nep::text').get().encode('utf-8'),
                'day_in_eng': r.css('span.eng::text').get().encode('utf-8'),
            }
            data.append(mydict)
        self.new_data.append({"month": month, "days": data})
        with open('data/{}.json'.format(self.year), 'w') as file:
            file.write(json.dumps(self.new_data, ensure_ascii=False))
