import requests
import time
from parsel import Selector
# from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        reponse = requests.get(url, timeout=3)
        time.sleep(1)
        if reponse.status_code != 200:
            return None
        return reponse.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    css_selector = "h2.entry-title a::attr(href)"
    html_page = Selector(html_content)
    array_links = html_page.css(css_selector).getall()

    return array_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
