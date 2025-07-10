from googlesearch import search
import pandas as pd
from typing import Any
import tiktoken


def get_urls(query: str, n_res: int, lang: str) -> list[str]:
    region = {'ru': 'RU',
              'en': 'US'}
    urls = [url for url in search(term=query, num_results=n_res, lang=lang, region=region[lang])]
    return urls

def infer_column_type(series: pd.Series, col) -> type:
    return series.unique(), col

def count_tokens(text, model='gpt-4o-mini'):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def calculate_cost(input_tokens, output_tokens, model="gpt-4o-mini"):
    # Расчет стоимости запроса на основе количества токенов
    rates = {
        "gpt-4o-mini": {"input": 1.1, "output": 4.4},
        "gpt-4.1-mini": {"input": 0.4, "output": 1.6}
    }
    
    input_cost = input_tokens * rates[model]["input"] / 1_000_000
    output_cost = output_tokens * rates[model]["output"] / 1_000_000
    
    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": input_cost + output_cost
    }

if __name__ == "__main__":
    print(count_tokens("Hello worlds"))