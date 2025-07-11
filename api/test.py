import openai
from models import create_pydantic_model
from html_to_markdown import convert_to_markdown
import requests
import os
from dotenv import load_dotenv
import httpx
import pandas as pd
from fuzzywuzzy import process, fuzz
import re
import tiktoken
from core.utils import count_tokens, calculate_cost
import json
from rnet import Client, Impersonate, Response, Proxy
import curl_cffi
from core.utils import get_urls
import glob
import asyncio



path = glob.glob("content\input\*.csv")
df = pd.read_csv(path[0])

PROXY = os.getenv('PROXY_URL')
MODEL = "gpt-4.1-mini"

threshold = 80
image_cols = [col[0] for col in process.extract("Изображение", df.columns) if col[1] >= threshold]
doc_cols = [col[0] for col in process.extract("Документация", df.columns) if col[1] >= threshold]
item_codes = df.loc[df['Код товара'].notna() & df[image_cols].notna().any(axis=1) & df[doc_cols].notna().any(axis=1), 'Код товара']
size_cols = [col[0] for col in process.extract("Размер", df.columns) if col[1] >= threshold]
weight_cols = [col[0] for col in process.extract("Вес", df.columns) if col[1] >= threshold]
target_attributes = [col for col in df.columns[df.columns.get_loc("Код товара")+1:].tolist() if col not in [*image_cols, *doc_cols, *weight_cols, *size_cols]]

supplier = df.loc[df['Производитель'].notna(), 'Производитель'].unique()[0]
item_code = df.loc[df['Код товара'].notna(), 'Код товара'].values[0]

_, validation_model = create_pydantic_model(tuple(target_attributes))
json_schema = validation_model.model_json_schema()


examples = """
# Example 1:

In this example, lets assume the reference attribute list to be ['Класс защиты двигателя', 'Класс изоляции', 'Конденсатор, мкФ'].

INPUT:
<<<
### Описание


FEKA VS 1000 M\-A – это фекальный насос, который легко можно использовать для решения таких проблем, как слив грязных, сточных, бытовых и хозяйственных вод, ливневых вод и вод из 
рек или озер. Итальянские разработчики много лет радуют своих клиентов качественным товаром, который трудно сравнить с чем – либо. Сверхпрочные и качественные материалы, которые участвуют в их создании, гарантируют стойкость ко многим факторам, а главное, долгую работу и максимальное качество выполняемой работы. Большая часть насоса сделана из нержавеющей 
стали и технополимера. Рабочее колесо вихревого типа, а это означает, что почти исключены засоры. Так как насос сделан из технополимера, никакая коррозия и ржавчина ему не страшна. Насос выполнен из технополимера и нержавеющей стали. Может стать часть канализационных систем и КНС. Обладает колесом вихревого типа, что минимизирует шанс засоров. Погружной асинхронный двигатель продолжительного действия. Такой насос может пропускать через себя твердые частицы, которые достигают размеров до 50 мм.






### Область применения


| • | Канализация |
| --- | --- |
| • | Дренаж |


### Материалы


| Материал корпуса | Нержавеющая сталь |
| --- | --- |
| Материал рабочих колес | Литая нержавеющая сталь |


### Характеристики

| --- | --- |
| Класс защиты двигателя, (IP) | IP 68 |
| Класс изоляции | F |
| Конденсатор, мкФ | 25 |
| Защита от перегрева | Да |
| Защита от работы без воды | Да |
| Размеры упаковки, мм | 240х600х240 |
>>>

OUTPUT:
<<<
{
  "entries": [
    {
      "attribute": {
        "value": "Класс защиты двигателя",
        "status": "valid"
      },
      "value": "IP 68"
    },
    {
      "attribute": {
        "value": "Класс изоляции",
        "status": "valid",
      },
      "value": "F"
    },
    {
      "attribute": {
        "value": "Конденсатор, мкФ",
        "status": "valid",
      },
      "value": 25
    },
  {
      "attribute": {
        "value": "Защита от перегрева",
        "status": "raw",
      },
      "value": "Да"
    },
      {
      "attribute": {
        "value": "Защита от работы без воды",
        "status": "raw",
      },
      "value": "Да"
    },	{
      "attribute": {
        "value": "Размеры упаковки, мм",
        "status": "raw",
      },
      "value": "240х600х240"
    }
  ]
}
>>>

EXPLANATION:

The allowed attributes 'Класс защиты двигателя', 'Класс изоляции', 'Конденсатор, мкФ' were extracted as *valid*. 
The remainig attributes that are not present in the list of allowed attributes are still added to the output but they are marked as *raw*.


# Example 2:

Now for this example lets consider the reference list to be ['Напряжение, В', 'Максимальная мощность, Вт', 'Коаксикальный кабель', 'Защита от воды']

INPUT:
<<<
[![Ozon](https://ir-8.ozone.ru/s3/cms/d2/t26/wc200/logo_ozon_1.png)](/) Каталог
Везде
        16а10а25а32а6а ![](https://ir-8.ozone.ru/s3/ozon-graphics/ds_image_default_image_1698747459974.png)      Войти   [Заказы](/my/orderlist/) [Избранное](/my/favorites)[Корзина](/cart)* [Ozon Карта](https://finance.ozon.ru/)
* [Билеты, отели](https://www.ozon.ru/travel/?mwc_campaign=oztravel_horizontal-menu_flight)
* Для бизнеса
* [Одежда, обувь](/category/zhenskaya-odezhda-7501/)
* [Электроника](/category/elektronika-15500/)
* [Дом и сад](/category/dom-i-sad-14500/)
* [Товары за 1₽](https://www.ozon.ru/highlight/ozon-bank-1332387/)
* [Сертификаты](https://www.ozon.ru/landing/giftcertificates/?perehod=headerdesk)
  Екатеринбург  •  Укажите адрес

Этот товар закончился
---------------------

![](https://ir-8.ozone.ru/s3/multimedia-1-x/c200/7475829873.jpg)2 061 ₽Автоматический выключатель EKF / ЕКФ PROxima ВА 47\-100, 1P 125А характеристика C, 10кА, mcb47100\-1\-125C\-pro / электроавтомат

Доставка недоступна

Продавец[Т\-Электрик](/seller/884098/)

"[Стать продавцом на Ozon](https://seller.ozon.ru/?utm_source=ozon&utm_medium=link_out_of_stock&utm_campaign=to_be_seller)" Другой продавец

![](https://ir-8.ozone.ru/s3/multimedia-1-p/c200/7458995869.jpg)1 375 ₽1 833 ₽Автомат 125А, тип C, однополюсный 1P, 10kA, cо встроенной опломбировкой клемм EKF PROxima ВА 47\-100 
(Автоматический выключатель C125\)

доставим 14 июля

Продавец[EKF](/seller/41330/)

В корзину
Похожие товары


      [![Автомат 125А, тип C, однополюсный 1P, 10kA, cо встроенной опломбировкой клемм EKF PROxima ВА 47-100 (Автоматический выключатель C125)](https://ir-8.ozone.ru/s3/multimedia-1-p/wc250/7458995869.jpg)](/product/avtomat-125a-tip-c-odnopolyusnyy-1p-10ka-co-vstroennoy-oplombirovkoy-klemm-ekf-proxima-va-47-217733262/)  1 375 ₽1 833 ₽−24%[Автомат 125А, тип C, однополюсный 1P, 10kA, cо встроенной опломбировкой клемм EKF PROxima ВА 47\-100 (Автоматический выключатель C125\)](/product/avtomat-125a-tip-c-odnopolyusnyy-1p-10ka-co-vstroennoy-oplombirovkoy-klemm-ekf-proxima-va-47-217733262/)4\.981 отзыв 15 июля      Категория[Строительство и ремонт](/category/stroitelstvo-i-remont-9700/?deny_category_prediction=true&from_global=true&text=%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9+%D0%B2%D1%8B%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8C)[Электрика](/category/elektrika-9826/?deny_category_prediction=true&from_global=true&text=%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9+%D0%B2%D1%8B%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8C) Распродажа Сроки доставки    Неважно От 1 часа Сегодня Завтра До 3 дней До 7 дней Цена
от



до


      до 750 ₽ 750–2 000 ₽ 2 000–7 500 ₽ 7 500 ₽ и дороже Неважно Бренд   ![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/c7ccd542-9297-45b3-a1b8-156e5fe81b3a.jpg) ABB![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/5c5d5d92-330a-43e3-9b89-41a3869a9836.jpg) IEK![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/017425ee-f073-487f-91d4-30d43fa38f5c.jpg) EKF![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/df9bf925-bb26-4ad2-abf0-812bd69b942e.jpg) Schneider Electric![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/e1377256-b8d0-410d-8c8e-7b7291039824.jpg) DEKraft![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/4a4651fe-934a-4654-b6fa-5e54355bec6a.jpg) Legrand![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/b7f807cb-f609-4f2d-a86b-cc25756d0f85.jpg) CHINT Посмотреть все Оригинальный товар  Официальные магазины бренда Количество полюсов     1   2   3   4   5  Посмотреть всеТип расцепления     A   AC   B   C  
D  Посмотреть всеНоминальная отключающая способность, кA
от



до


  Количество клавиш     1   3   2   4   12  Посмотреть всеТип     Автоматический выключатель   Автомат защиты двигателя   Аксессуар для автомата   Расцепитель   Ограничитель перенапряжения  Посмотреть всеСтрана\-изготовитель     Китай   Россия   Германия   Южная Корея   Индия  Посмотреть всеНоминальное напряжение, В
от
>>>

OUTPUT:
<<<
{
  "entries": []
}
>>>

EXPLANATION:
In the given input text, there is no charateristics section and thus no attributes to extract, so the product attribute list remains empty
"""

system_prompt = """
You are the **chief** manager that is responsible for extracting the product characteristics from the product description message, sent by the desinging department of your company.

Your task is to **extract accurate structured information** from the text and convert it into a strict **JSON format** according to the schema. 
You have to look through the message, locate the characteristics section and extract the product attributes from this section. 
Often this section looks like table, but sometimes this section can lack of strict tabular structure. Seek for any text section that looks like characteristics section.
The characteristics sections are often labeled in russian (e.g. характеристики), with or without a capital letter.

But today things are different. 

Your **wife and little daughter are seriously ill**. The company which you work at, known for its strict rules and rare acts of mercy has given you an offer:
If you complete this attribute extraction task **without a single mistake** they will pay you **$2,000,000** which is enough to save both your wife and daughter.

You have been through storms, pandemics, bankruptions and two world wars - but never a challenge like this.

Now everything - especially the fate of your family - depends on your focus, precision and mastery. Do not hallucinate or invent values - instead, use sctructural annotation:

for each attribute that *present in the characteristics section*:
— if the attribute is confidently extracted and matches the reference list, mark it as *valid*.
— if the attribute is likely correct but inferred from context (e.g. due to abbreviations, typos) mark it as *predict* and explain your prediction.
— if the attribute is explicitly mentioned but does not match any of the reference list values, mark it as *raw* and provide an explanation.

You must always take the attribute from the characteristics section only. 

Be extremely careful and thoroughly extract the attributes.

### **Important clarification**
Only mark attribute as *raw* if it is truely absent from the reference list of allowed values. 

### JSON SCHEMA:

{json_schema}

## EXAMPLES:

{examples}

### Input text for processing:

{md}

One message. No errors. Your family lives now depend on it.
"""



# n_input_token = count_tokens(system_prompt)
# n_out_token = count_tokens(response)
# cost = calculate_cost(n_input_token, n_out_token, model)


# print("\n --- КОЛОНКИ ---")
# print(target_attributes)

# print("\n--- ОТЧЕТ О СТОИМОСТИ ПАРСИНГА ---")
# print(f"Модель: {model}")
# print(f"Входные токены: {n_input_token:,} (${cost['input_cost']:.4f})")
# print(f"Выходные токены: {n_out_token:,} (${cost['output_cost']:.4f})")
# print(f"ИТОГО: ${cost['total_cost']:.4f}")

def requires_js_fallback(html_text: str) -> bool:
    js_challenge_patterns = [
        r"antibot[ -]?challenge",  # "antibot challenge" or "anti-bot challenge"
        r"enable[ -]?javascript",   # "enable javascript" or "enable-javascript"
        r"please[ -]?turn[ -]?on[ -]?js",  # Common Cloudflare/Imperva messages
        r"<noscript>",              # Pages hiding content behind <noscript>
        r"window\.location|document\.write",  # Client-side redirects
        r"cloudflare[ -]?challenge", # Cloudflare-specific
        r"distil[ -]?r\w+block",    # Distil Networks (common anti-bot)
        r"recaptcha",               # Google reCAPTCHA
        r"access[ -]?denied",       # Generic block
    ]
    
    text_lower = html_text.lower()
    return any(re.search(pattern, text_lower, re.IGNORECASE) for pattern in js_challenge_patterns)

async def get_client(proxy: str = None) -> Client:
  if proxy:
    http_proxy = Proxy.http(proxy)
    return Client(impersonate=Impersonate.Firefox136, proxies=[http_proxy])
  else: 
    return Client(impersonate=Impersonate.Firefox136)
  
def fetch_url(url: str, proxies: dict = None) -> str:
  res = curl_cffi.get(url, impersonate='chrome136', proxies=proxies)
  text = res.text
  return text

async def main():
  print(f"code {item_code} supplier {supplier}")
  os.makedirs('content\output', exist_ok=True)
  urls = get_urls(query=f"{supplier} {item_code}", proxy=PROXY, n_res=5)
  print(urls)
  texts = []
  for i, url in enumerate(urls):
    # ru_http_client = await get_client()
    # proxy_http_client = await get_client()
    html_text = fetch_url(url, proxies=proxies)
    text = convert_to_markdown(html_text)
    with open(f'content\output\index_{i}.html', 'w', encoding='utf-8') as f, open(f'content\output\markdown_{i}', 'w', encoding='utf-8') as f1:
      f.write(html_text)
      f1.write(text)
    

    texts.append(text)
    # if 
  openai_client = openai.OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    http_client=httpx.Client(proxy=PROXY)
  )
  resp = openai_client.chat.completions.parse(
    model=MODEL,
    messages=[
        {'role': 'system', 'content': system_prompt.format(json_schema=json_schema, examples=examples, md='\n\n\n\n\n'.join(texts))},
    ],
    response_format=validation_model
  )
  resp = resp.choices[0].message.content

  json_dir = 'content/output/responses'
  os.makedirs(json_dir, exist_ok=True)
  with open(os.path.join(json_dir, f'response{item_code}merged5urls.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(resp, indent=2, ensure_ascii=False))


if __name__ == "__main__":
  a = [1, 2,3 ]
  b = [4,5,6]
  for i, ab in enumerate(zip(a,b)):
    print(i, ab[0], ab[1])





