from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}
    return [(news["title"], news["url"])
            for news in search_news(query)]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        iso_date = datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")

    formated_date = datetime.strftime(iso_date, "%d/%m/%Y")
    news = search_news({"timestamp": formated_date})
    return [(new["title"], new["url"]) for new in news]


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
