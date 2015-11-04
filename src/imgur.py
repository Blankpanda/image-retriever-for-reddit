import requests, urllib
from bs4 import BeautifulSoup

def get_album_ids(urls):
    album_ids = []
    for url in urls:
        reverse_url = url[::-1]
        url_id =  reverse_url.split("/")[0]
        album_ids.append(url_id)
    return album_ids

def download_imgur_album(urls):
    album_ids = get_album_ids(urls)
    count = 0
    for url in urls:
        html_source = requests.get(url).text
        soup = BeautifulSoup(html_source, "html.parser")
        matches = soup.select('.album-view-image-link a')
        for match in matches:
            imageUrl = match['href']
            urllib.request.urlretrieve('http:' + imageUrl, test + str(count) + ".jpg")

            # if os.path.exists("tagless"):
            #     download_image_tagless_append(
            #     imageUrl,
            #     album_ids[count]
            #     )
            # else:
            #     download_image_tagless(
            #     imageUrl,
            #     album_ids[count]
            #     )
            count += 1
