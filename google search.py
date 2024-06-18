from googlesearch import search

query = input("Query : ")

for url in search(query):
    print(url)
    
    