import requests
import time
import json

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://www.gooood.cn",
    "priority": "u=1, i",
    "referer": "https://www.gooood.cn/",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
cookies = {
    "language": "zh_CN",
    "Hm_lvt_dc9dffedd71420cbc8e2dd8d6bd0bbfe": "1756822809",
    "HMACCOUNT": "7CF9CF99FAC80E52",
    "Hm_lvt_f6653282260d1fe6d7858f62178e3b18": "1756822809",
    "_gid": "GA1.2.1275587804.1756822809",
    "_gat_gtag_UA_240434465": "1",
    "Hm_lpvt_dc9dffedd71420cbc8e2dd8d6bd0bbfe": "1756822939",
    "Hm_lpvt_f6653282260d1fe6d7858f62178e3b18": "1756822939",
    "_ga": "GA1.2.1854961725.1756822808",
    "FCNEC": "%5B%5B%22AKsRol_F0hE8KMfmKg6RbgoxMjfgNSQOR2m-mUGorNbd9Fjt3gGcmQlAqlyaRezC1q-rxzeVQn8xDQ_ZB3TQCDvMDfdWvSQhKSMy3V5JUbCIabZqugibDIUZIycnq2BCglzdNoG5FUeJCWc58GQ8WQwBuO1gCD_4Dg%3D%3D%22%5D%5D",
    "_ga_CH5FSBW2P3": "GS2.1.s1756822808$o1$g1$t1756822947$j7$l0$h0"
}
url = "https://dashboard.gooood.cn/api/wp/v2/posts"

params = {
    "categories": "8",
    "page": "2",
    "per_page": "18"
}

for page in range(1, 4):
    params["page"] = str(page)
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.json())
    print(response)
    time.sleep(2)
