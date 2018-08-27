import requests
import re
from tk import Py4Js
import random
from urllib.parse import urlencode
class google_translate():
    def __init__(self,content):
        self.content=content
        js=Py4Js()
        tk=js.getTk(self.content)
        self.tk=tk
    def translate(self):
        data = {
            "client":"t",
            "sl":"en",
            "tl": "zh-CN",
            "hl": "zh-CN",
            "dt": "at",
            "dt": "bd",
            "dt": "ex",
            "dt": "ld",
            "dt": "md",
            "dt": "qca",
            "dt": "rw",
            "dt": "rm",
            "dt": "ss",
            "dt": "t",
            "ie": "UTF-8",
            "oe": "UTF-8",
            "source": "bh",
            "ssel": "0",
            "tsel": "0",
            "kc": "1",
            "tk": self.tk,
            "q": self.content,
        }
        params = urlencode(data)
        base = 'https://translate.google.cn/translate_a/single'
        url = base + '?' + params
        print(url)
        pro = ['101.132.122.230:3128']
        head = {
            'cookie':'GA1.3.1462919132.1529804283; _gid=GA1.3.297361377.1529804283; 1P_JAR=2018-6-24-9; NID=133=MRl70Fz3P3H7JAPCmT3uqA_im1ixRFK_EPKL5GtKoV9tSVVQaRG0rJn1pxZMMAO9RN40wJr9hd56r2RjeP-B3PmNfRcoE7Hir9D8XSzVCRi_bMGpJIAIkGkZKHVbNefz',
            'accept-encoding':'gzip, deflate, br',
            'x-client-data': 'CIy2yQEIorbJAQjEtskBCKmdygEIqKPKAQ ==',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
        string = requests.get(url,proxies={'http':pro[0]},headers=head).text
        return re.findall('.*?"(.*?)"',string,re.S)[0]





