# "roots": {
#       "bookmark_bar": {
#          "children": [ {
#             "children": [ {
#                "children": [ {
#                   "children": [ {
#                      "date_added": "13213963879741810",
#                      "guid": "3189f7e6-bdab-48ce-8385-86ebd05168d6",
#                      "id": "368",
#                      "name": "Swagger local",
#                      "sync_transaction_version": "2661",
#                      "type": "url",
#                      "url": "http://localhost:64695/swagger/index.html"
#                   }

import json


class Favorite():
    def __init__(self, type, id, name, url):
        self.name = name
        self.id = id
        self.type = type
        self.url = url

    def __str__(self):
        return 'id:' + self.id + " " + self.name


favorites = {}


def get_favorite(obj):
    if 'type' in obj and obj["type"] == "url":
        return Favorite(obj["type"], obj["id"], obj["name"], obj["url"])


def loop(data):
    children = get_children(data)

    print(type(children))
    for item in children:
        obj = get_favorite(item)
        if obj is not None:
            favorites[obj.id] = obj
            print(item)
        else:
            loop(item)


def get_children(obj):
    if 'children' in obj:
        return obj['children']


with open('bookmarks.json') as json_file:
    data = json.load(json_file)
    data = data["roots"]["bookmark_bar"]
    loop(data)

favorites = {k: v for k, v in favorites.items() if v.url == v.name}
a = 1
