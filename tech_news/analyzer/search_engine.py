from tech_news import database
from datetime import datetime


def serialize_news(news):
    return [(new["title"], new["url"]) for new in news]


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    options = {
        "title": 1,
        "url": 1,
        "_id": 0,
    }
    search_news = list(database.db.news.find(query, options))

    return serialize_news(search_news)


# Requisito 7
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": formatted_date, "$options": "i"}}
    options = {
        "title": 1,
        "url": 1,
        "_id": 0,
    }
    search_news = list(database.db.news.find(query, options))

    return serialize_news(search_news)


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    options = {
        "title": 1,
        "url": 1,
        "_id": 0,
    }
    search_news = list(database.db.news.find(query, options))

    return serialize_news(search_news)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
