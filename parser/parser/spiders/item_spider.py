import scrapy
import re
import openai
from pydantic import BaseModel
import requests
from parser.utils import get_urls
import os
from html_to_markdown import convert_to_markdown


class ItemSpider(scrapy.Spider):
    name = "item_spider"

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url for url in url]


    # def start(self):


    def parse(self, response):
        md = convert_to_markdown(response.text)
        yield {         
            'url': response.url,
            'html': response.text,
            'md': md
        }

