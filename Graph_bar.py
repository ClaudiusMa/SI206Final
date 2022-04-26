import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import sqlite3







dic = {"The Complete Idiot's Guide to Learning Yiddish": '4.11', "Heinerman's Encyclopedia of Healing Juices": '4.07', 'Super Healing Foods': '4.00', "The Supervisor's Big Book of Lists": '5.00', 'A Brief Tour of Human Consciousness': '4.02', "Heinerman's New Encyclopedia of Fruits & Vegetables": '4.44', 'The Disciplined Trader': '4.16', '101 Biggest Mistakes Managers Make and How to Avoid Them': '3.50', 'How to Eat Away Arthritis': '3.04', 'Psycho-Cybernetics 2000': '3.81', 'Brain Builders!': '2.92', "Heinerman's Encyclopedia of Healing Herbs & Spices": '4.13', "The First-Time Supervisor's Survival Guide": '3.40', 'Hidden Power': '3.89', 'Conversational Power': '3.66', 'The Miracle of Mind Dynamics': '4.16', 'Secrets of Closing Sales': '3.89', 'Unlimited Selling Power': '3.81', 'Wisdom of the Mystic Masters': '4.13', 'Winning Office Politics': '3.98', 'Your Infinite Power to Be Rich': '4.05', 'The Reason Why': '3.97', 'Under the Net': '3.77', 'The Sandcastle': '3.88', 'A Severed Head': '3.75', 'The Unicorn': '4.16', 'The Nice and the Good': '3.85', 'An Accidental Man': '3.79', 'The Sacred and Profane Love Machine': '3.90', 'Design of Cities': '4.03', 'The Human Figure': '4.25', 'The Dharma Bums': '3.92', 'On the Road': '3.62', 'Steinbeck': '3.88', "One Flew Over the Cuckoo's Nest": '4.20', 'Karl Marx': '3.62', 'The Way of the Storyteller': '3.93', 'Stop-Time': '3.85', 'The Book of the Hopi': '4.07', 'Sometimes a Great Notion': '4.24', 'The Conservationist': '3.34', 'The Lives of a Cell': '4.15', 'Thus Spoke Zarathustra': '4.06', 'The Face of Battle': '4.13', 'Exterminator!': '4.38', 'The Bereaved Parent': '4.24', 'The Death of Woman Wang': '3.46', 'The Measure of My Days': '3.97', 'Travels with Charley in Search of America': '4.06', 'To Change China': '3.89', 'Bridgeport Bus': '2.88', "Burger's Daughter": '3.53', 'A Nervous Splendor': '3.98', "The Dragon's Village": '3.25', '1066': '4.05', 'Waiting for the Barbarians': '3.94', "July's People": '3.52', 'Deep Blues': '4.21', 'In the Heart of the Country': '3.68', 'The Gate of Heavenly Peace': '4.00', "Billy Phelan's Greatest Game": '3.94', 'Legs': '4.18', 'Ordinary People': '3.92', 'The Year of Living Dangerously': '3.89', 'Farewell to the Sea': '4.04', 'The Women of Brewster Place': '4.18', 'The Puzzle Palace': '3.89', 'My Soul Is Rested': '4.49', 'The First Rumpole Omnibus': '4.32', 'Clinging to the Wreckage': '3.95', 'Ironweed': '3.86', 'Run with the Horsemen': '4.31', 'O Albany!': '3.83', 'The Neverending Story': '4.17', 'Life and Times of Michael K': '3.86', 'The Little Disturbances of Man': '4.03', 'Stones for Ibarra': '4.00', 'White Noise': '3.87', 'Nights at the Circus': '3.90', 'Filters against Folly': '4.27', "Quinn's Book": '3.75', 'Greasy Lake and Other Stories': '3.94', 'Dreams of Sleep': '4.23', 'The Art of the Tale': '4.07', 'The Memory Palace of Matteo Ricci': '3.81', 'The Solace of Open Spaces': '4.14', 'Pilgrims in Their Own Land': '3.90', 'The Whisper of the River': '4.30', 'A Sport of Nature': '3.76', 'Empire Express': '3.94', 'Forced Entries': '3.90', 'Demon Box': '4.11', 'End Zone': '3.66', 'The Needs of Strangers': '3.84', 'The Origins of the American Constitution': '3.63', 'Linden Hills': '4.05', 'Wedding Readings': '2.84', 'The Bone People': '4.05', "Q's Legacy": '4.02', 'The Second Rumpole Omnibus': '4.48', 'Saints and Strangers': '3.93', 'Between Women': '3.73', 'Writing in Restaurants': '3.73', 'Sweetness and Power': '3.79', 'Amongst Women': '3.94', 'Singing from the Well': '3.92', 'Interzone': '3.75', 'The Letters of William S. Burroughs': '4.18', 'My Education': '3.29', 'The Western Lands': '4.06'}


def graph_top3(dic):
    sorted_d = dict(sorted(dic.items(), key=lambda item: item[1],reverse=False))


    lst = []
    for key in sorted_d.keys():
        lst.append(key)

    x = np.array(lst[-3:])
    y = np.array(list(sorted_d.values())[-3:])

    #plt.ylim(ymin=0,ymax=5)
    
    plt.bar(x,y,color = "hotpink")
    
    plt.xlabel('Book Name')
    plt.ylabel("Rating")
    plt.title('Top 3 Rating Books')

    plt.show()

graph_top3(dic)