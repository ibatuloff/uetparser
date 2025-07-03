from parser.parser.spiders.item_spider import ItemSpider

from scrapy.crawler import CrawlerProcess
import os
import json
import csv
import shutil
import argparse
from glob import glob


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="uetparser"
    )
    parser.add_argument("--path", help='путь до файла который нужно заполнить')
    args = parser.parse_args()

    # Создаем директории input и output
    input_path = './content/input'
    os.makedirs(input_path, exist_ok=True)

    output_path = './content/output'
    os.makedirs(output_path, exist_ok=True)

    csv_file = glob(os.path.join(input_path, "*.csv"))
    if not csv_file:
        shutil.move(args.filepath, input_path)
    
    with open(*csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        item_codes = [row.get("Код товара") for row in reader]
        item_supplier = [row.get("Производитель") for row in reader]
        attrs = reader.fieldnames
        for code, supplier in zip(item_codes, item_supplier):
            urls = get_urls(query=f"{supplier} {code}")
            spider = ItemSpider(
                urls=urls,
                attributes=attrs
            )

# TODO проверить что паук запускается
    
if __name__=="__main__":
    main()

