from bs4 import BeautifulSoup
import requests

repose = requests.get("http://www.cnblogs.com/yoyoketang/")

blog = repose.content
# print(1,type(blog))

soup = BeautifulSoup(blog, "html.parser", from_encoding='utf-8')
# print(type(soup))
# print(soup.attrs)
# times = soup.find_all(class_='day')
# print(3, type(times))
# print(times)
# for i in times:
#     print(i.div.content[0])
# print(soup.get_text)
# print(times.children)#打印节点
# times = soup.li
# for descendant in times.descendants:
#     for i in descendant:
#         print(i.string)
# print(times.contents[0])
# for j in times.contents:
#     print(j.string)
# test_date = soup.find_all(class_='dayTitle')
# for k in test_date:
#     print(k.a.string)
# soup.find_all()
# for string in soup.strings:
#     print(repr(string))
# for string in soup.stripped_strings:
#     print(string)
for string in soup.find_all('li'):
    print(string.string)