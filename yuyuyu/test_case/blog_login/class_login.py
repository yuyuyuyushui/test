import requests, re

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class login:
    def __init__(self, url1):
        self.obj_sesion = requests.session()
        self.url1 = url1

    def login(self, json_date):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
        }
        respose_obj = self.obj_sesion.post(self.url1, headers=headers, json=json_date)
        print(respose_obj.content)
        return respose_obj.json()

class blog(login):
    def __init__(self, url2_save):
        super(blog, self).__init__()
        self.url2 = url2_save

    def save(self, title, body_date):
        '''保存草稿箱：
               参数1：title  # 标题
               参数2：body   # 中文
        '''
        body_ = {"__VIEWSTATE": "",
                "__VIEWSTATEGENERATOR": "FE27D343",
                "Editor$Edit$txbTitle": title,
                "Editor$Edit$EditorBody": "<p>" + body_date + "</p>",
                "Editor$Edit$Advanced$ckbPublished": "on",
                "Editor$Edit$Advanced$chkDisplayHomePage": "on",
                "Editor$Edit$Advanced$chkComments": "on",
                "Editor$Edit$Advanced$chkMainSyndication": "on",
                "Editor$Edit$lkbDraft": "存为草稿",
                 }
        response_obj = self.obj_sesion.post(self.url2, data=body_, verify=False)
        return response_obj.url

    def get_postid(self):
        postid = re.findall(r"postid=(.+?)&", self.url2)
        return postid[0]

    def delete_box(self, url3, postid):
        '''删除草稿箱'''
        json3 = {"postId": postid}
        response_obj  = self.obj_sesion.post(url3, json=json3, verify=False)
        print(response_obj.json())


if __name__ == "__main__":
    url_1 = "https://passport.cnblogs.com/user/signin"
    payload = {
        "input1": "xxx", "input2": "xxx",
        "remember": True
    }
    login_json = blog(url_1).login(payload)