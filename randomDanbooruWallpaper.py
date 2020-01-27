# grabs a random wallpaper-sized image from Danbooru
# and sets it as the desktop wallpaper

import setWallpaper
import os
import requests
import key

temp_dir = os.getcwd()
user = key.user
api_key = key.api_key

# get random wallpaper-size image from Danbooru

# request one random wallpaper-sized image from danbooru
danbooru_posts = "https://danbooru.donmai.us/posts.json"
# danbooru_posts = "https://safebooru.donmai.us/posts.json"
parameters = {
              "limit" : 1, 
              "random" : "true", 
              "tags" : "score:>=5 ratio:1.7..2 height:>=1080 -rating:e"
             }

print("Requesting random image")
response = requests.get(danbooru_posts, auth=(user, api_key), params=parameters)
response.raise_for_status()
data = response.json()
image_url = data[0]['file_url']

print("Downloading image")
image_response = requests.get(image_url)
image_response.raise_for_status()

wallpaper_name = "temp"
wallpaper_path = os.path.join(temp_dir, wallpaper_name)
try:
    with open(wallpaper_path, "wb") as wallpaper_file:
        for chunk in image_response.iter_content(100000):
            wallpaper_file.write(chunk)
except IOError:
    print("Failed to create file.")

# set image as wallpaper
print("Setting wallpaper")
setWallpaper.set_wallpaper(wallpaper_path)

# cleanup by removing the temp file
try:
    os.remove(wallpaper_path)
except IOError:
    print("Failed to delete temp file.")