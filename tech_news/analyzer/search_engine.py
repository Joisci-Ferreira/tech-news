from tech_news.database import search_news
from datetime import datetime


def newsElements(news_list):
    formatted_news_list = []

    for news in news_list:
        formatted_news = (news["title"], news["url"])
        formatted_news_list.append(formatted_news)

    return formatted_news_list


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_list = search_news({
        "title": {
            "$regex": title,
            "$options": "i"
        }
    })

    return newsElements(news_list)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news_list = search_news({"timestamp": (date.strftime("%d/%m/%Y"))})

    return newsElements(news_list)


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    news_list = search_news({
        "tags": {
            "$regex": tag,
            "$options": "i"
        }
    })

    return newsElements(news_list)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
