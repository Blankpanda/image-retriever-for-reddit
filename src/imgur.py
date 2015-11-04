import requests, urllib
from bs4 import BeautifulSoup

def get_album_ids(urls):
    album_ids = []
    for url in urls:
        reverse_url = url[::-1]
        url_id =  reverse_url.split("/")[0]
        album_ids.append(url_id)
    return album_ids

def download_imgur_album(url):
    print("SX")
    count = 0
    html_source = requests.get(str(url)).text
    soup = BeautifulSoup(html_source, "html.parser")
    matches = soup.find_all('meta')
    for match in matches:
        print(match.get('content'))
    #    urllib.request.urlretrieve('http:' + imageUrl, "test_" + str(count) + ".jpg")
        count += 1
