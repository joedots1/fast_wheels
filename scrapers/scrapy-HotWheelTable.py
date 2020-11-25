import scrapy

"""" Scrapes the hotwheels.fandom wiki of Hot wheels by year
    scrape the resulting page in the 
    url pattern wiki/List_of_{year}_Hot_Wheels
"""

year = 2020


class ScrapeTableSpider(scrapy.Spider):
    name = "scrape-table"
    # allowed_domains = ["https://getbootstrap.com/docs/4.0/content/tables"]
    start_urls = [f"https://hotwheels.fandom.com/wiki/List_of_{year}_Hot_Wheels"]

    def start_requests(self):
        urls = [
            f"https://hotwheels.fandom.com/wiki/List_of_{year}_Hot_Wheels",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//*[@class="wikitable"]//tbody/tr'):
            yield {
                "toy_num": row.xpath("td[1]//text()").extract(),
                "col_num": row.xpath("td[2]//text()").extract(),
                "model": row.xpath("td[3]//text()").extract(),
                "series": row.xpath("td[4]//text()").extract(),
                "series_num": row.xpath("td[5]//text()").extract(),
                "photo_url": row.css("a.image::attr(href)").extract(),
                "year": str(year),
            }


# scrapy runspider scrapers/scrapy-HotWheelTable.py -o car_data/cars_2009.json --nolog
