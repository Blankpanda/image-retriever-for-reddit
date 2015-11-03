import beautifulsoup4

client_id = 'YOUR CLIENT ID'
client_secret = 'YOUR CLIENT SECRET'

client = ImgurClient(client_id, client_secret)

def get_album_ids(urls):
    album_ids = []
    for url in urls:
        reverse_url = url[::-1]
        url_id =  reverse_url.split("/")[0]
        album_ids.append(url_id)
    return album_ids

def imgur_album(urls):
    album = client.get_album(id)
    for x in album:
        print(x.link)
