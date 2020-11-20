import unittest

from project import parser


def test_put_any_website():
    l = ('https://www.google.com', 'https://yandex.ru/news/?utm_source=main_stripe_big', 'https://mignews.com/')
    for url in l[:2]:
        news = parser.collectNews(url)
        assert len(news) == 0
    news = parser.collectNews(l[2])
    assert len(news) > 0


def test_generate_table_on_wrong_input():
    l = ('1', 3, (3, 5, 76, 8), parser.collectNews('https://mignews.com/'))
    for val in l[:3]:
        htmlcode = parser.generate_table(val)
        assert htmlcode == ""
    htmlcode = parser.generate_table(l[3])
    assert len(htmlcode) > 0
