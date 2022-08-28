from tech_news import database
from datetime import datetime


def serialize_news(news):
    return [(new["title"], new["url"]) for new in news]


def get_news(param, field):
    query = {}
    query[field] = {"$regex": param, "$options": "i"}
    options = {
        "title": 1,
        "url": 1,
        "_id": 0,
    }
    search_news = list(database.db.news.find(query, options))

    print(search_news)

    return serialize_news(search_news)


# Requisito 6
def search_by_title(title):
    return get_news(title, "title")


# Requisito 7
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
    except ValueError:
        raise ValueError("Data inválida")

    return get_news(formatted_date, "timestamp")


# Requisito 8
def search_by_tag(tag):
    return get_news(tag, "tags")


# Requisito 9
def search_by_category(category):
    return get_news(category, "category")
