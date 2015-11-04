import requests, urllib,os
from bs4 import BeautifulSoup
from downloader import *

def get_album_id(url):
    reverse_url = url[::-1]
    url_id =  reverse_url.split("/")[0]
    return url_id

def download_imgur_album(url):

    count = 0
    html_source = requests.get(str(url)).text
    soup = BeautifulSoup(html_source, "html.parser")
    matches = soup.find_all("meta")

    for match in matches:
        if "http://i.imgur.com" in match.get('content'):
            scraped_url = match.get('content')
            id = get_album_id(url)

            if os.path.exists(id):
                download_album_image_append(scraped_url,
                id,
                count
                )
            else:
                download_album_image(scraped_url,
                id,
                count
                )
            count += 1
