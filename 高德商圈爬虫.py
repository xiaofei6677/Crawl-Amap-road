import pandas as pd
import time
import requests
while True:
    t = time.strftime("%H%M%S", time.localtime())
    r =requests.get("http://report.amap.com/ajax/districtRank.do?linksType=3&cityCode=510100")
    s=r.json()
    a=[]
    for i in range(len(s)):
        for j in range(len(s[i]['coords'][0][0])):
            a.append([s[i]['coords'][0][0][j]['lon'],s[i]['coords'][0][0][j]['lat'],s[i]['name'],s[i]['index'],s[i]['speed'],s[i]['number']])
    c = pd.DataFrame(a)
    c.to_csv(t+'new.csv')
    time.sleep(300)
