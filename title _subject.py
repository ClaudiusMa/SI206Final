import json
import unittest
import os
import requests


# Get titles and output the subjects

def read_list(lst):
    dic = {}
    for item in lst:
        topic = request(item)
        if topic in dic.keys():
            dic[topic].append(item)

        else:
            dic[topic]=[item]
    print(dic)
    return dic


def find_type(api_return):

    type_list = api_return["results"][0]["subjects"]
    for item in type_list:
        if "--" in item:
            lst = item.split(" -- ")
            type = lst[1]
            return type




def request(bookname):
    bookname.lower()
    base_url = "https://gutendex.com/books/?"
    para = "search=" + str(bookname)
    url = base_url + para
    r = requests.get(url)
    dict = json.loads(r.text)
    type = find_type(dict)
    return type

lst = ["Great Expectations", "Deathworld","Harry's Ladder to Learning"]
read_list(lst)
