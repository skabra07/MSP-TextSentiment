"""Docstring."""
import newspaper
import string
from textRecognition import text_sentiment

def download_article(url):
    count = 0
    try:
        article = newspaper.Article(url)
        article.download()
        while(True):
            if(article.html != ''):
                break
        article.parse()
        while(True):
            if(article.text != '' and article.title != ''):
                break
            count += 1
            if count > 50:
                break
        article.nlp()
        count = 0
        while(True):
            if(article.keywords != ''):
                break
            count += 1
            if count > 50:
                break
    except newspaper.ArticleException:
        return
    text = article.text
    return text


def run(url):
    text = download_article(url)
    result = text_sentiment(text)
    print("The score for this article is: {}".format(result))
    return result
