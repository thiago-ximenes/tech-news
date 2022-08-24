import requests
import parsel
from time import sleep


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
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
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(text=html_content)
    link = selector.css(
        "div.nav-links a.next.page-numbers::attr(href)"
    ).get()
    print(link)
    return link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
