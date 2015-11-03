import urllib, os

def download_image(url, folder_name, id):
    os.makedirs(folder_name)
    urllib.request.urlretrieve(url, folder_name + "/"
    + "img_" + str(id) + ".jpg")

def append_image_to_existing_directory(url,folder_name,id):
    urllib.request.urlretrieve(url, folder_name + "/"
    + "img_" + str(id) + ".jpg")
