from ctypes import create_string_buffer
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
import json
import sqlite3

def get_info_lists():
    # https://developer.penguinrandomhouse.com/member/register
    api_key = 'jnn6wze242eg9fj63cu67ycu' #use link in line above to register and get an api_key
    url = f"https://api.penguinrandomhouse.com/resources/v2/title/domains/PRH.US/titles?preferLanguage=E&rows=234&api_key={api_key}"
    source = requests.get(url).text
    
    source_dict = json.loads(source) #converts string to a disctionary to access keys values

    

    list_of_dictionaries = source_dict['data']['titles'] #key 'titles' holds a list of dictionaries containing all data
    title_list, isbn_list, author_list = [], [], [] #empty list to be filled while looping list above

    count = 0
    for x in list_of_dictionaries: #each book entry data 
        
        if x['author'] == 'Penguin Merchandise':
            count+=1
        else:
            title_list.append(x['title']) #adds corresponding title value for this book instance
            isbn_list.append(x['isbn']) #adds corresponding isbn value for this book instance
            author_list.append(x['author']) #adds corresponding author value for this book instance


    return title_list


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
        dic[item]=topic
    return dic


def find_type_fromAPI(api_return):

    type_list = api_return["results"][0]["subjects"]
    for item in type_list:
        if "--" in item:
            lst = item.split(" -- ")
            API_result = lst[1]
            return API_result



def get_types(booktitles, CACHE_FNAME):
    booktitles.lower()
    base_url = "https://gutendex.com/books/?"
    para = "search=" + str(booktitles)
    url = base_url + para
    CACHE = read_cache(CACHE_FNAME)

    if url in CACHE:
        print("caching sucess")
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
            return "Unknown"

def replace_types(link):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False          
    url = link
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    bigtype = soup.find(class_="bigBoxContent containerWithHeaderContent")
    if bigtype == None:
        return "Unknown"
    else:
        minitype = bigtype.find(class_="actionLinkLite")
        type = minitype.contents[0]
        return type


def get_ratings_from_goodreads(link):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False          
    url = link
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    minirating = soup.find(class_="minirating")

    rating = minirating.contents[1]
    rating = rating.split()[0]
    return rating

def create_table_titles(conn, cur):
    cur.execute('CREATE TABLE IF NOT EXISTS Titles (id INTEGER, title TEXT)')
    conn.commit()

def create_table_genres(conn, cur):
    cur.execute('CREATE TABLE IF NOT EXISTS Genres (id INTEGER, genre TEXT)')
    conn.commit()

def create_table_ratings(conn, cur):
    cur.execute('CREATE TABLE IF NOT EXISTS Ratings (id INTEGER, rating REAL)')
    conn.commit()

def create_table_new_genres(conn, cur):
    cur.execute('CREATE TABLE IF NOT EXISTS New_Genres (id INTEGER, genre TEXT)')
    conn.commit()


def insert_table_titles(conn, cur, titles, id):
    for book in titles:
        cur.execute('INSERT INTO Titles (id, title) VALUES (?,?)', (id, book))
        id = id + 1
    conn.commit()

def insert_table_genres(conn, cur, genres, id):
    for book in genres.keys():
        cur.execute('INSERT INTO Genres (id, genre) VALUES (?,?)', (id, genres[book]))
        id = id + 1
    conn.commit()

def insert_table_ratings(conn, cur, ratings, id):
    for book in ratings.keys():
        cur.execute('INSERT INTO Ratings (id, rating) VALUES (?,?)', (id, ratings[book]))
        id = id + 1
    conn.commit()

def insert_table_new_genres(conn, cur, genres, id):
    for book in genres.keys():
        cur.execute('INSERT INTO New_Genres (id, genre) VALUES (?,?)', (id, genres[book]))
        id = id + 1
    conn.commit()


def find_alt_genres(conn, cur):
    cur.execute("""
    SELECT n.genre, n.id FROM New_Genres n
    JOIN Genres g
    ON n.id = g.id
    WHERE g.genre = "Unknown" or g.genre = "None"
    """)
    res = cur.fetchall()
    return res

def update_genres(conn, cur, tobe_updated):
    for tups in tobe_updated:
        book = tups[1]
        genre = tups[0]
        cur.execute(f"""
        UPDATE Genres
        SET genre = '{genre}'
        WHERE id = '{book}'
        """)
        conn.commit()

def fetch_updated_genres(conn, cur):
    cur.execute("""
    SELECT genre FROM Genres
    """)
    res = cur.fetchall()
    return res

def select_ratings(conn, cur, genre):
    cur.execute(f"""
    SELECT r.rating FROM Ratings r
    JOIN Genres g
    ON r.id = g.id
    WHERE g.genre = '{genre}'
    """)
    res = cur.fetchall()
    return res


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/final.db')
    cur = conn.cursor()

    book_titles = get_info_lists()
    book_titles = book_titles[:110]
    print(book_titles)
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CACHE_FNAME = dir_path + '/' + "cache_itunes.json"
    book_types = title_to_type(book_titles, CACHE_FNAME)
    print(book_types)
    new_book_types = {}
    for book in book_types.keys():
        #if book_types[book] == "Unknown" or book_types[book] == "None" or book_types[book] == None:
        link = "https://www.goodreads.com/search?utf8=%E2%9C%93&query=" + book
        newtype = replace_types(link)
        new_book_types[book] = newtype
    
    book_ratings = {}
    for book in book_titles:
        link = "https://www.goodreads.com/search?utf8=%E2%9C%93&query=" + book
        rating = get_ratings_from_goodreads(link)
        print(book)
        print(rating)
        book_ratings[book] = rating
    print(book_ratings)

    cur.execute("DROP TABLE IF EXISTS Titles")
    create_table_titles(conn, cur)
    cur.execute("DROP TABLE IF EXISTS Genres")
    create_table_genres(conn, cur)
    cur.execute("DROP TABLE IF EXISTS Ratings")
    create_table_ratings(conn, cur)
    cur.execute("DROP TABLE IF EXISTS New_Genres")
    create_table_new_genres(conn, cur)
    head = 0
    tail = 24
    for i in range(5):
        sub_titles = book_titles[head: tail]
        sub_type = dict(list(book_types.items())[head: tail])
        sub_rating = dict(list(book_ratings.items())[head: tail])
        sub_new_type = dict(list(new_book_types.items())[head: tail])
        insert_table_titles(conn, cur, sub_titles, head)
        insert_table_genres(conn, cur, sub_type, head)
        insert_table_ratings(conn, cur, sub_rating, head)
        insert_table_new_genres(conn, cur, sub_new_type, head)
        head = head + 25
        tail = tail + 25

    new_genres = find_alt_genres(conn, cur)
    print(new_genres)
    update_genres(conn, cur, new_genres)
    all_genres = fetch_updated_genres(conn, cur)
    print(all_genres)
    final_genres = []
    for genre in all_genres:
        ngenre = genre[0]
        if ngenre not in final_genres:
            final_genres.append(ngenre)
    print(final_genres)
    
    genre_rating = {}
    for genre in final_genres:
        ratings = select_ratings(conn, cur, genre)
        total = float(0)
        count = 0
        print(ratings)
        if len(ratings) != 0:
            for rat in ratings:
                total += rat[0]
                count = count + 1
            avg = total /count
            genre_rating[genre] = avg
    print(genre_rating)
    
if __name__ == "__main__":
    main()

