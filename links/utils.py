import requests
from bs4 import BeautifulSoup


def fetch_link_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    og_title = soup.find('meta', property='og:title')
    og_description = soup.find('meta', property='og:description')
    og_image = soup.find('meta', property='og:image')

    return {
        'title': og_title['content'] if og_title else soup.title.string,
        'description': og_description['content'] if og_description else '',
        'image': og_image['content'] if og_image else '',
    }
