
import matplotlib.pyplot as plt
import numpy as np

dic={'religion': 1, 'non-fiction': 35, 'cookbooks': 2, 'business': 2, 'reference': 1, 'Unknown': 4, 'self-help': 1, 'psychology': 1, 'Early works to 1800': 1, 'Drama': 1, 'Guidebooks': 1, 'History': 2, 'Fiction': 47, 'fantasy': 1, 'West (U.S.)': 1, 'romance': 1, 'Economic conditions': 1, 'Social life and customs': 1, 'United States': 1, 'Scotland': 1}

def graph(dic):

    y = np.array(list(dic.values()))
    mylabels = list(dic.keys())

    plt.pie(y, labels = mylabels)
    plt.show() 

graph(dic)


