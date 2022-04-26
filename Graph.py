import matplotlib
import matplotlib.pyplot as plt
import os
import sqlite3

dict = {'religion': 4.11, 'non-fiction': 3.9711764705882358, 'cookbooks': 4.0649999999999995, 'business': 4.25, 'reference': 4.44, 'Unknown': 3.3025, 'self-help': 3.66, 'psychology': 3.81, 'Early works to 1800': 3.77, 'Drama': 4.16, 'Guidebooks': 3.62, 'History': 3.855, 'Fiction': 3.955, 'fantasy': 3.83, 'West (U.S.)': 4.07, 'romance': 2.84, 'Economic conditions': 3.73, 'Social life and customs': 3.94, 'United States': 3.29, 'Scotland': 4.06}


def graph(dict):

    lst = []
    for key in dict.keys():
        lst.append(key)

    plt.barh(lst, dict.values(), align='center')

    plt.xticks([1,2,3,4])
    plt.xlabel('Average Rating')
    plt.ylabel("Book Genres")
    plt.title('Average rating of Different Book Genres')

    plt.show()

graph(dict)