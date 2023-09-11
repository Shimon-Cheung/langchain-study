# -*-  coding: utf-8 -*-
import csv
import json
from urllib.parse import quote
from urllib.request import urlopen
from tools.xlsx_tools import read_excel

# address = ["福州市仓山区城门镇城门村城门街359号"]


def getlnglat(address):
    url = "http://api.map.baidu.com/geocoding/v3/"
    output = "json"
    ak = "TmMEiHDnLCl1tHb9yWOMI5gv168XpIv3"
    add = quote(address)  # 由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + "?" + "address=" + add + "&output=" + output + "&ak=" + ak
    req = urlopen(uri)
    res = req.read().decode()  # 将其他编码的字符串解码成unicode
    temp = json.loads(res)  # 对json数据进行解析
    return temp


f = open("city.csv", "w", encoding="utf-8", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["city", "lng", "lat"])

addr = read_excel("files/第二批供电所.xlsx")
for i in addr["Sheet1"]:
    temp = f'{i["市"]}市{i["区县"]}{i["城镇"]}{i["供电所"]}'
    print(temp)
    lng = getlnglat(temp)["result"]["location"]["lng"]  # 采用构造的函数来获取经度
    lat = getlnglat(temp)["result"]["location"]["lat"]  # 获取纬度
    str_temp = [temp, lng, lat]
    csv_writer.writerow(str_temp)  # 写入文档
f.close()
