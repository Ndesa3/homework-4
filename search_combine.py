#import data_load
import indexer 
import searcher

query=input("query: ")
query = query.strip(" ").split() #get rid of the front and rear spaces, space being the delimiter
web_query = []
query = list(set(query))
web_query = query[:]

d = indexer.get_traversal_data("raw_data.pickle.txt")
searcher.search(d,query)
w = indexer.get_traversal_data("web_data.pickle.txt")
searcher.search(w,web_query)

