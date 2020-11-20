from bs4 import BeautifulSoup
import requests


def collectNews(url, hot = True):
    news = []
    page = requests.get(url)
    if(page.status_code != 200):
        return news
    soup = BeautifulSoup(page.text, "html.parser")
    news = soup.findAll('div', class_='lenta')
    if hot:
        return  generate_table(news)
    else:
        return  generate_table(news, 'time2')


def generate_table(news, nameToFind = 'time2 time3'):
    try:
        if len(news) == 0:
            return
    except:
        return
    htmltext = "<table>\n"
    for i in range(len(news)):
        if news[i].find('a', class_= nameToFind) is not None:
            htmltext += "<tr>\n<td>"
            htmltext += news[i].text[0:6]
            htmltext += "</td>\n<td>"
            htmltext += news[i].text[6:] + "</td>\n</tr>\n"
    htmltext += "\n</table>\n"
    return htmltext


if __name__ == "__main__":
    url = "https://mignews.com/"
    print(collectNews(url))
    pass
