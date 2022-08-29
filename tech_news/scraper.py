import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
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


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css(".comment-body").getall())
    summary = "".join(
        selector.css(".entry-content > p:first-of-type ::text").getall()
    ).strip()
    tags = selector.css('.post-tags a[rel="tag"]::text').getall()
    category = selector.css(".meta-category span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
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
