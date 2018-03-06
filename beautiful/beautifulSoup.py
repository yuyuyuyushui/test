from bs4 import BeautifulSoup
import requests

repose = requests.get("http://www.cnblogs.com/yoyoketang/")

blog = repose.content

soup = BeautifulSoup(blog, "html.parser")

times = soup.find_all(class_="dayTitle")
print(type(times))
for i in times:
    a = i
    print(i.a.string)