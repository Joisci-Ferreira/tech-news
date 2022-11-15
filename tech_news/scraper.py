import requests
import time
from parsel import Selector


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
    css_selector = "a.next.page-numbers::attr(href)"
    html_page = Selector(html_content)
    next_page = html_page.css(css_selector).get()

    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    comments_count = len(selector.css("comment-list").getall())
    summary = "".join(
        selector.css(
            "div.entry-content > p:nth-of-type(1) *::text"
        ).getall()
    ).strip()
    tags = selector.css("a[rel='tag']::text").getall()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
