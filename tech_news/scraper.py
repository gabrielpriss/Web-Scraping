import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        req = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
    except requests.Timeout:
        return None
    if (req.status_code != 200):
        return None
    return req.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    list = []
    selector = Selector(text=html_content)
    for url in selector.css("a.cs-overlay-link").xpath('@href').getall():
        list.append(url)
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    url = selector.css("a.next").xpath('@href').get()
    return(url)
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
