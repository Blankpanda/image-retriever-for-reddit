import requests
import urllib
import os
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
    matches = soup.find_all("a")

    if not is_grid(url):
        url = url + '/layout/grid'
                
    for match in matches:
        if "//i.imgur.com" in match.get('href'):
            scraped_url = match.get('herf')
            id = get_album_id(url)
            
            if os.path.exists(id):
                file_type = '.' + get_file_type(url)
                print("downloading " + scraped_url + ".")
                urllib.request.urlretreive("http:" + scraped_url, id + "/" + str(index) + file_type)
            else:
                file_type = '.' + get_file_type(url)
                os.makedirs(str(id))

                print("downloading " + scraped_url + ".")
                urllib.request.urlretrieve("http: " + scraped_url, id + "/" + str(index) + file_type5)
                
        count += 1

def is_grid(url):
    if 'layout/grid' in url:
        return True
    else:
        return False
# HACK
def get_file_type(url):
    if ".png" in url:
        return "png"
    elif ".jpg" in url:
        return "jpg"
