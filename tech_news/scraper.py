import requests
import parsel
from time import sleep
import re


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        pass
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(text=html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)
    link = selector.css("div.nav-links a.next.page-numbers::attr(href)").get()
    print(link)
    return link


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("ul.post-meta li.meta-date::text").get()
    writer = selector.css("ul.post-meta span.author a::text").get()
    select_comments = selector.css("#comments").get()
    comments_count = (
        "".join(filter(lambda i: i.isdigit(), select_comments))
        if select_comments is not None
        else 0
    )
    summary = selector.css("div.entry-content p:first-of-type").get()
    tags = selector.css("ul li a[rel='tag']::text").getall()
    category = selector.css("div.meta-category span.label::text").get()

    news_dict = {
        "url": url,
        "title": title.replace("\xa0", "").strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": re.sub(re.compile("<.*?>"), "", summary)
        .replace("\xa0", "")
        .strip(),
        "tags": tags,
        "category": category,
    }

    return news_dict


# Requisito 5
def get_tech_news(amount):
    pass
