import scrapy
import re

class ItemPropertySpider(scrapy.Spider):
    name = "item_parser"

    def __init__(self, urls=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.starting_urls = urls 
        self.target_attributes = attributes

    def start_requests(self):
        for url in self.starting_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        text = " ".join(response.xpath("//body//text()").getall()).lower()
        text = re.sub(r"\s+", " ", text)

        found = {}
        for prop in self.target_attributes:
            pattern = rf"{prop}\s*[:=]?\s*([0-9\.]+(?:\s*(?:v|a|ohm|hz|w))?)"
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                found[prop] = match.group(1)

        if found:
            yield {
                "url": response.url,
                "attributes": found
            }
        else:
            self.logger.info(f"No target attributes found on {response.url}")
