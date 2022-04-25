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
from Finalproject_Booktitle import get_info_lists
from title_subject import read_list, find_type, read_list


