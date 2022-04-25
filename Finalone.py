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

from final_project import get_ratings_from_goodreads
from 

link = "https://www.goodreads.com/search?utf8=%E2%9C%93&query=frankenstein"
get_ratings_from_goodreads((link))
