from googlesearch_python import search


def get_urls(query: str) -> list[str]:
    urls = [url for url in search(query)]
    return urls