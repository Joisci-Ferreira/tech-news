from tech_news.database import search_news


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


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
