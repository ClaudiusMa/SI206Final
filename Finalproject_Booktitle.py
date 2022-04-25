import requests
import json

def get_info_lists():
    # https://developer.penguinrandomhouse.com/member/register
    api_key = 'Make Your Key' #use link in line above to register and get an api_key
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


    return title_list, isbn_list, author_list, count

titles, isbns, authors, num_skipped = get_info_lists()
print(f"We skipped {num_skipped} elements because they were examples from Peguin Merchandise")
print()
print(len(titles), titles)
print()
print(len(isbns), isbns)
print()
print(len(authors), authors)