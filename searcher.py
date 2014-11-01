import os
import time

def search(d, query):
    count = 0
    if ("or" in query) and ("and" not in query):
        query.remove("or")
        print("Performing OR search for: ", query)
        for i in d:
            for q in query:
                if q in i[1]:
                    count = count + 1
                    print ("Found at", (i[0]))
                    print ('\n')
                    #print ("Last modifed: ",time.ctime(os.path.getmtime(i[0])))
                    #print ("File size: ",os.path.getsize(i[0])," bytes")
                    print ('\n')
                    break
        if count == 0:
            print("Not found")
    elif(len(query)==1):
        count = 0
        for i in d:
            for q in query:
                if q in i[1]:
                    count = count +1                    
                    print ("Found at", (i[0]))
                    print ('\n')
                    print ("Last modifed: ",time.ctime(os.path.getmtime(i[0])))
                    print ("File size: ",os.path.getsize(i[0])," bytes")
        if count == 0:
            print("Not Found")
    elif (("and" in query) and ("or" not in query)) or (('and' not in query) and ("or" not in query)):
        if 'and' in query:
            query.remove("and")
        print("Performing AND search for: ", query)
        query_len = len(query)
        succuss = 0
        for i in d:
            for q in query:
                if q in i[1]:
                    succuss = succuss + 1
            if query_len == succuss:
                print ("Found at", (i[0]))
                print ('\n')
                print ("Last modifed: ",time.ctime(os.path.getmtime(i[0])))
                print ("File size: ",os.path.getsize(i[0])," bytes")
                print ('\n')
            succuss = 0
        if not succuss == query_len :
            print("Not found")
        
    
