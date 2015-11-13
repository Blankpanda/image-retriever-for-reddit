import urllib, os

bad_characters = ["<", ">", ":", "/", "\\", "|", "?", "*" , '"']
file_types = ["jpg", "png", "gif"]

def download_image(url, folder_name, id):

    file_type = get_file_type(url)
    url = add_file_type(url)

    for character in bad_characters: # the tag has bad characters in it
        if character in folder_name:
            folder_name = folder_name.replace(character, "")

    os.makedirs(folder_name)

    try:
        print("downloading " + url)
        urllib.request.urlretrieve(url, folder_name + "/"
        + "img_" + str(id) + file_type)
    except Exception as e:
        # os.remove(path_name)
        print(url + "is not an image.  Skipping.")

def download_image_append(url,folder_name,id):

    file_type = "." + get_file_type(url)
    url = add_file_type(url)

    try:
        print("downloading " + url)
        urllib.request.urlretrieve(url, folder_name + "/" + "img_"
        + str(id) + file_type)
    except Exception as e:
        print(url + "is not an image.  Skipping.")


def download_image_tagless(url,id):

    file_type = "." + get_file_type(url)
    url = add_file_type(url)

    folder_name = "tagless"

    os.makedirs(folder_name)

    try:
        print("downloading " + url)
        urllib.request.urlretrieve(url, older_name + "/"
        + "img_" + str(id) + file_type)
    except Exception as e:
        print(url + "is not an image.  Skipping.")


def download_image_tagless_append(url,id):

    file_type = "." + get_file_type(url)
    url = add_file_type(url)

    folder_name = "tagless"


    try:
        print("downloading " + url)
        urllib.request.urlretrieve(url, folder_name + "/" + "img_"
        + str(id) + file_type)
    except Exception as e:
        print(url + "is not an image.  Skipping")


def download_album_image(url,id, index):

    print("in album: " + id)

    file_type = "." + get_file_type(url)

    os.makedirs(str(id))

    try:
        print(" downloading " + url )
        urllib.request.urlretrieve(url, id + "/" + str(index) + file_type)
    except Exception as e:
        print(" " + url + "is not an image.  Skipping") # this should never happen.


def download_album_image_append(url,id, index):

    file_type = "." + get_file_type(url)

    try:
        print(" downloading: " + url)
        urllib.request.urlretrieve(url, url, id + "/" + str(index) + file_type)
    except Exception as e:
        print(" " + url + "   is not an image.  Skipping") # again this should never happen


def get_file_type(url):
    if ".png" in url:
        return "png"
    elif ".jpg" in url:
        return "jpg"
    elif ".gif" in url:
        return ".gif"
    else:
        return "jpg"

def add_file_type(url):
    for ftype in file_types:
        if ftype in url:
            return url
        else:
            return url + ".jpg" # this is the best way to catch most images
