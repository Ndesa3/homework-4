import urllib.request
from urllib.error import  URLError
import re
import pickle
mylist=[]
def visit_url(url, domain,mylist):
	global crawler_backlog
	if(len(crawler_backlog)>100):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("Processing:", url)
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=page.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)

			if result:
				title = result.group("title")
				tup = (url,title)
				mylist.append(tup)
				f1=open("web_data.pickle.txt","bw")
				pickle.dump(mylist,f1)
				f1.close()
				print(title)

			result = regexp_keywords.search(content_string, re.IGNORECASE)

			if result:
				keywords = result.group("keywords")
				tup = (url,title)
				mylist.append(tup)
				f1=open("web_data.pickle.txt","bw")
				pickle.dump(mylist,f1)
				f1.close()
				print(keywords)

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain,mylist)
	except URLError as e:
		print("error")


crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu",mylist)
