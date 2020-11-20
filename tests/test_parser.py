import unittest

from project import parser


def test_put_any_website():
    incorrect = ('https://www.google.com', 'https://yandex.ru/news/?utm_source=main_stripe_big')
    correct = 'https://mignews.com/'
    for url in incorrect:
        news = parser.collectNews(url)
        assert len(news) == 0
    news = parser.collectNews(correct)
    assert len(news) > 0


def test_generate_table_on_wrong_input():
    incorrect = ('1', 3, (3, 5, 76, 8))
    correct = parser.collectNews('https://mignews.com/')
    for val in incorrect:
        htmlcode = parser.generate_table(val)
        assert htmlcode == ""
    htmlcode = parser.generate_table(correct)
    assert len(htmlcode) > 0
