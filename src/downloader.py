import urllib, os

def download_image(url, folder_name, id):
    os.makedirs(folder_name)
    urllib.request.urlretrieve(url, folder_name + "/"
    + "img_" + str(id) + ".jpg")

def download_image_append(url,folder_name,id):
    urllib.request.urlretrieve(url, folder_name + "/"
    + "img_" + str(id) + ".jpg")

def download_image_tagless(url,id):
    folder_name = "tagless"
    os.makedirs(folder_name)
    urllib.request.urlretrieve(url, folder_name + "/"
    + "img_" + str(id) + ".jpg")

def download_image_tagless_append(url,id):
    folder_name = "tagless"
    urllib.request.urlretrieve(url, folder_name + "/"
    + "img_" + str(id) + ".jpg")
