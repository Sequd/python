import json
import urllib.request
import re

json_name = 'bookmarks3.json'
all_favorites = {}


class Favorite:
    def __init__(self, type, id, name, url):
        self.name = name
        self.id = id
        self.type = type
        self.url = url
        self.title = None

    def __str__(self):
        return 'id:' + self.id + " " + self.name


def get_favorite(obj):
    if 'type' in obj and obj["type"] == "url":
        return Favorite(obj["type"], obj["id"], obj["name"], obj["url"])


def loop_load(data):
    children = get_children(data)
    if children is not None:
        for item in children:
            obj = get_favorite(item)
            if obj is not None:
                all_favorites[obj.id] = obj
                print(item)
            else:
                loop_load(item)
    else:
        if isinstance(data, dict):
            for k, v in data.items():
                loop_load(v)


def get_children(obj):
    try:
        if 'children' in obj:
            return obj['children']
    except:
        return None


with open(json_name) as json_file:
    json_data = json.load(json_file)

# bookmark_bar = json_data["roots"]["bookmark_bar"]
loop_load(json_data)

favorites = {k: v for k, v in all_favorites.items() if v.name.startswith("http")}

pattern = '<title>(.+?)</title>'
pattern = re.compile(pattern)
for k, v in favorites.items():
    try:
        with urllib.request.urlopen(v.url) as response:
            encoding = response.info().get_param('charset', 'utf8')
            html = response.read().decode(encoding)
            titles = re.findall('<title>(.+?)</title>', html)
            if len(titles) > 0:
                print('Title of:' + v.url)
                print(titles[0])
                v.title = titles[0]
    except:
        print("cant load url: " + v.url)

favorites = {k: v for k, v in favorites.items() if v.title is not None}
print(len(favorites))


def loop_write(data):
    children = get_children(data)
    if children is not None:
        for item in children:
            obj = get_favorite(item)
            if obj is not None and favorites.get(obj.id) is not None:
                item["name"] = favorites.get(obj.id).title
                print('replace name-url to title: ' + item["name"])
            else:
                loop_write(item)
    else:
        if isinstance(data, dict):
            for k, v in data.items():
                loop_write(v)


loop_write(json_data)

with open(json_name, 'w') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False)
