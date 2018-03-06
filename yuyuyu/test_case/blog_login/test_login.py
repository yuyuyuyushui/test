import requests
def login(sesion_obj, url, payload):
    '''登录'''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://passport.cnblogs.com/user/signin',
    'Content-Type': 'application/json; charset=utf-8',
    'VerificationToken': '@TokenHeaderValue()',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '557',
    'Cookie': '_ga=GA1.2.1278342048.1519534021; '
              '_gid=GA1.2.1920975253.1519534021;'
              ' SERVERID=b9b9402740b573694788a8e7dd5b5c26|1519661490|1519657392;'
              ' ASP.NET_SessionId=r5vo5l4ounwjuyejhqwukapc; _gat=1',
    'Connection': 'keep-alive'
               }
    r = sesion_obj.post(url, json=payload, headers=headers, verify=False)
    result = r.json()
    print(result)
    return result['success'] # 返回True或False
def save_box(sesion_obj, url2, title, body_data):
    '''# 获取报存之后url地址'''
    body = {"__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR": "FE27D343",
            "Editor$Edit$txbTitle": title,
            "Editor$Edit$EditorBody": "<p>"+body_data+"</p>",
            "Editor$Edit$Advanced$ckbPublished": "on",
            "Editor$Edit$Advanced$chkDisplayHomePage": "on",
            "Editor$Edit$Advanced$chkComments": "on",
            "Editor$Edit$Advanced$chkMainSyndication": "on",
            "Editor$Edit$lkbDraft": "存为草稿",
            }
    r2 = sesion_obj.post(url2, data=body, verify=False)
    print(r2.url)
    return r2.url


def get_postid(u):
    '''正则提取postid'''
    import re
    postid = re.findall(r"postid=(.+?)&", u)
    print(postid) # 这里是list
    if len(postid) < 1:
        return ''
    else:
        return postid[0]


def delete_box(s,url3, postid):
    '''删除草稿箱'''
    json3 = {"postId": postid}
    r3 = s.post(url3, json=json3, verify=False)
    print(r3.json())


if __name__ == "__main__":
    url = "https://passport.cnblogs.com/user/signin"
    payload = {
        "input1": "xxx","input2": "xxx",
        "remember": True
    }
    s = requests.session()
    login(s, url, payload)
    url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    u = save_box(s, url2, "标题", "正文内容")
    postid = get_postid(u)
    url3 = "https://i.cnblogs.com/post/delete"
    delete_box(s, url3, postid)
