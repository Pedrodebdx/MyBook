# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:17:09 2020

@author: utilisateur
"""
import requests
import json
###############################################################

r_books = requests.get('https://demo.api-platform.com/books?order[publicationDate]=desc&page=1')
response_data = r_books.json() 
data = list(response_data["hydra:member"][:10])
for i in range(10):
    print(response_data["hydra:member"][i]['title'])


    

############################################################


r_author = requests.get('https://demo.api-platform.com/books?author=Dr.%20Kaitlyn%20Ratke&page=1')
author_data = r_author.json() 

for i in range(len(author_data["hydra:member"])):
    print(author_data["hydra:member"][i]['title'])


###############################################################

book_id = requests.get('https://demo.api-platform.com/books/1d52ba85-97c8-4cc3-b81a40582f3aff64/reviews?page=1')
r_book_id = book_id.json() 
for i in range(len(r_book_id["hydra:member"])):
    b = r_book_id["hydra:member"][i]['body']
    print(f'Commentaire n°{i}:  {b}')

###############################################################

data = {
  
  "body": "AAAAAAAAAAAAAAAAAAAAAAAAAA",
  "rating": 5,
  "book": "/books/1d52ba85-97c8-4cc3-b81a40582f3aff64",
  "author": "Pierre",
  "publicationDate": "2020-01-10T00:00:00.0000"
}



url = 'https://demo.api-platform.com/reviews'

request = requests.post( url , json=data)
p = request.json()


###############################################################

data2 = {
  
  "body": "REEEEE--------------AAAAAAAA",
  "rating": 5,
  "book": "/books/1d52ba85-97c8-4cc3-b81a40582f3aff64",
  "author": "Pierre",
  "publicationDate": "2020-01-10T00:00:00.0000"
}

p_id = p['@id'].split('/')[-1]
url = 'https://demo.api-platform.com/reviews/'+ p_id



request2 = requests.put( url, json= data2)

print(request2.text) #TEXT/HTML
print(request2.status_code, request2.reason) #HTTP
