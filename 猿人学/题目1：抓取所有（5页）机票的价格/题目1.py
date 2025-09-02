

import requests

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/1",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36 Edg/139.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "rs8xg8j3i1myi5oqzt1kym5sqljzeu3z",
    "qpfccr": "true",
    "no-alert3": "true",
    "tk": "-4911410997706853071"
}
url = "https://match.yuanrenxue.cn/api/match/1"
params = {
    "page": "2",
    "m": "b80d738b16a4a69761dcb5ef512f2d4b丨1756924176"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)