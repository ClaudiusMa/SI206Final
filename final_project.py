#Group Member: Chuxuan Ma, Zhen Qin, Jeannie Szomstein
#This is a local version of Zhen Qin's website portion: goodreads.com
import string
from xml.sax import parseString
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import requests
import re
import os
import csv
import unittest

def get_ratings_from_goodreads(link):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False          
    url = link
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    minirating = soup.find(class_="minirating")
    print(minirating)
    rating = minirating.contents[1]
    rating = rating.split()[0]
    print(rating)
    return rating


def main():
    link = "https://www.goodreads.com/search?utf8=%E2%9C%93&query=frankenstein"
    get_ratings_from_goodreads((link))
    

if __name__ == "__main__":
    main()