import requests
import execjs
import json

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/1",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36 Edg/140.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
url = "https://match.yuanrenxue.cn/api/match/1"

# 读取 JS 文件内容
with open('gateway.js', 'r', encoding='utf-8') as f:
    js_source = f.read()
# 编译整个脚本（创建一个 JS 上下文）
ctx = execjs.compile(js_source)
# 调用函数
m = ctx.call('getM')

ans = 0
page = 1
count = 0
try:
    while True:
        params = {
            "page": f"{page}",
            "m": m
        }
        response = requests.get(url, headers=headers, params=params)
        data = json.loads(response.text)["data"]
        for dt in data:
            ans += dt['value']
            count += 1
        page += 1
except:
    print(ans/count)