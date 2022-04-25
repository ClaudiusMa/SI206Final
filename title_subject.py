import json
import unittest
import os
import requests


# Get titles and output the subjects - Chuxuan Ma

def read_cache(CACHE_FNAME):

    try:
        file = open(CACHE_FNAME, "r")
        content = file.read()
        Jdata = json.loads(content)
        file.close()
        return Jdata
    except:
        return {}

def write_cache(CACHE_FNAME, CACHE):

    file = open(CACHE_FNAME, "w")
    data = json.dumps(CACHE)
    file.write(data)
    file.close()


def title_to_type(lst, CACHE_FNAME):
    dic = {}
    for item in lst:
        topic = get_types(item, CACHE_FNAME)
        if topic in dic.keys():
            dic[topic].append(item)

        else:
            dic[topic]=[item]
    print(dic)
    return dic


def find_type_fromAPI(api_return):
    try: 
        type_list = api_return["results"][0]["subjects"]
        for item in type_list:
            if "--" in item:
                lst = item.split(" -- ")
                API_result = lst[1]
                return API_result
    except:
        print("This book is not in our database")



def get_types(booktitles, CACHE_FNAME):
    booktitles.lower()
    base_url = "https://gutendex.com/books/?"
    para = "search=" + str(booktitles)
    url = base_url + para
    CACHE = read_cache(CACHE_FNAME)

    if url in CACHE:
        print("results from caching")
        return find_type_fromAPI(CACHE[url])
    
    else:
        try:
            r = requests.get(url)
            dict = json.loads(r.text)
            CACHE[url] = dict
            write_cache(CACHE_FNAME,CACHE)
            type = find_type_fromAPI(dict)
            return type
        except:
            print("Exception")
            return None


lst = ["Great Expectations", "Deathworld","Harry's Ladder to Learning"]
dir_path = os.path.dirname(os.path.realpath(__file__))
CACHE_FNAME = dir_path + '/' + "cache_itunes.json"
title_to_type(lst, CACHE_FNAME)
