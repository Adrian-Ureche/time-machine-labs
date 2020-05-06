# coding: utf-8
import typing
import logging
import urllib.request
import xml.etree.ElementTree as ET


logging.basicConfig(filename="hackernews.log", level=logging.DEBUG)


class Article(typing.NamedTuple):
    title: str
    url: str


def articles(url:str="https://news.ycombinator.com/rss") -> typing.List[Article]:
    content = urllib.request.urlopen(url).read()
    feed = ET.fromstring(content)
    result = [
        Article(element[0].text, element[1].text)
        for element in feed[0]
        if element.tag == "item"
    ]
    return result


for article in articles():
    print(f"{article.title}")
    print(f"{article.url}")