from pygooglenews import GoogleNews
import math

gn = GoogleNews()


approved_sources = ['The Athletic', 'Goal.com', 'talkSPORT', "The Times Herald", "AS USA", "Forbes", "USA TODAY", "El Futbolero USA", "Architectural Digest", "Reuters", "The Motley Fool", "Yahoo Finance", "Business Insider", "The Economist", "CNBC", "The Washington Post", "The New York Times", "CoinDesk", "Yahoo Sports", "ABC News", "CNN", "Bloomberg", "New York Magazine", "The Verge", "New York Post", "TechCrunch", "Macworld", "Apple", "9to5Mac", "AppleInsider", "CNET", "Microsoft", "WIRED"]

def get_keyword_news_support(keyword):
    if keyword == "":
        return
    count = 0
    articles = []
    search = gn.search(keyword, when='12h')
    for i in search['entries']:
        if count > 9:
            break
        source = i['title'].rsplit(" - ", 1)
        if source[1] in approved_sources:
            articles.append([i['title'], i['link']])
            count += 1
    return articles

def get_general_news():
    articles = []
    count = 0
    search = gn.search("", when='12h')
    for i in search['entries']:
        if count > 9:
            break
        source = i['title'].rsplit(" - ", 1)
        if source[1] in approved_sources:
            articles.append([i['title'], i['link']])
            count += 1
    return articles
