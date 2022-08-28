from tech_news import database


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    options = {
        "title": 1,
        "url": 1,
        "_id": 0,
    }
    search_news = list(database.db.news.find(query, options))

    serialized_news = [(new["title"], new["url"]) for new in search_news]

    return serialized_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
