import pandas as pd
import requests
import time
while True:
    t = time.strftime("%H%M%S", time.localtime())
    r =requests.get("http://report.amap.com/ajax/roadRank.do?roadType=0&timeType=0&cityCode=510100")
    s=r.json()
    a=[]
    for i in range(len(s["tableData"])):
        for j in range(len(s["tableData"][i]["coords"])):
            a.append([s["tableData"][i]["coords"][j]["lon"],s["tableData"][i]["coords"][j]["lat"],s["tableData"][i]['name'],s["tableData"][i]['index'],s["tableData"][i]['speed']])
    c = pd.DataFrame(a)
    c.to_csv(t+'road.csv')
    time.sleep(300)
