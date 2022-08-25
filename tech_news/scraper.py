import time
import requests
from parsel import Selector
from tech_news.database import create_news


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
    return (url)
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    # tags = []
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get(),
    timestamp = selector.css("li.meta-date::text").get()
    titulo = selector.css("h1.entry-title::text").get()
    writer = selector.css("a.n::text").get()
    comments = selector.css("div#comments > h5::text").get() or 0
    summary = selector.css("div.entry-content").xpath('p/text()').get()
    category = selector.css("span.label::text").get()
    tags = selector.css(
        "section[class='post-tags'] ul li a::text").getall() or []
    obj = {
        "url": url,
        "title": titulo,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments,
        "summary": summary,
        "tags": tags,
        "category": category
    }
    return obj


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    news = []
    url = "https://blog.betrybe.com/"
    while len(news) < amount:
        land_page_content = fetch(url)
        next_land_page_url = scrape_next_page_link(land_page_content)
        land_page_urls = scrape_novidades(land_page_content)
        for page_url in land_page_urls:
            if len(news) == amount:
                break
            current_new_content = fetch(page_url)
            new_data = scrape_noticia(current_new_content)
            news.append(new_data)
        url = next_land_page_url
    create_news(news)
    return news
