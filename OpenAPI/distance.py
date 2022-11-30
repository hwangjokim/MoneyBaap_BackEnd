import pandas as pd
from urllib.parse import urlparse
import json
import requests

# 서울대학교
class SNU:
    dest = ""
    start = "서울특별시 관악구 관악로 1"
    def __init__(self, address):
        self.dest = address

    def getDist(self):
        # 출발점 좌표 구하기
        url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?" + "query=" + SNU.start
        res = requests.get(urlparse(url).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj = res.json()
        xStart = json_obj['addresses'][0]['x']
        yStart = json_obj['addresses'][0]['y']

        #도착점 좌표 구하기
        url2 = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?" + "query=" + SNU.dest
        res2 = requests.get(urlparse(url2).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj2 = res2.json()
        xDest = json_obj['addresses'][0]['x']
        yDest = json_obj['addresses'][0]['y']

        #거리 구하기
        url3 = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?" + "start=" + str(xStart) + "," + str(yStart) + "&goal=" + str(xDest) + "," + str(yDest) + "&option=trafast"
        res3 = requests.get(urlparse(url3).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj3 = res3.json()

        return str(json_obj3['route']['trafast'][0]['summary']['distance']) + "m"

# 중앙대학교
class CAU:
    dest = ""
    start = "서울특별시 동작구 흑석로 84"
    def __init__(self, address):
        self.dest = address

    def getDist(self):
        # 출발점 좌표 구하기
        url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?" + "query=" + CAU.start
        res = requests.get(urlparse(url).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj = res.json()
        xStart = json_obj['addresses'][0]['x']
        yStart = json_obj['addresses'][0]['y']

        #도착점 좌표 구하기
        url2 = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?" + "query=" + CAU.dest
        res2 = requests.get(urlparse(url2).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj2 = res2.json()
        xDest = json_obj['addresses'][0]['x']
        yDest = json_obj['addresses'][0]['y']

        #거리 구하기
        url3 = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?" + "start=" + str(xStart) + "," + str(yStart) + "&goal=" + str(xDest) + "," + str(yDest) + "&option=trafast"
        res3 = requests.get(urlparse(url3).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj3 = res3.json()

        return str(json_obj3['route']['trafast'][0]['summary']['distance']) + "m"

# 숭실대학교
class SSU:
    dest = ""
    start = "서울특별시 동작구 상도로 369"
    def __init__(self, address):
        self.dest = address

    def getDist(self):
        # 출발점 좌표 구하기
        url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?" + "query=" + SSU.start
        res = requests.get(urlparse(url).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj = res.json()
        xStart = json_obj['addresses'][0]['x']
        yStart = json_obj['addresses'][0]['y']

        #도착점 좌표 구하기
        url2 = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?" + "query=" + SSU.dest
        res2 = requests.get(urlparse(url2).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj2 = res2.json()
        print(json_obj2)

        xDest = json_obj2['addresses'][0]['x']
        yDest = json_obj2['addresses'][0]['y']
        
        #거리 구하기
        url3 = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?" + "start=" + str(xStart) + "," + str(yStart) + "&goal=" + str(xDest) + "," + str(yDest) + "&option=trafast"
        res3 = requests.get(urlparse(url3).geturl(), headers={"X-NCP-APIGW-API-KEY-ID": "secret_id", "X-NCP-APIGW-API-KEY": "secret_key"})
        json_obj3 = res3.json()
        print(json_obj3)

        return str(json_obj3['route']['trafast'][0]['summary']['distance']) + "m"

test = SSU("서울 관악구 관악로28길 2 2층 플란타")
print(test.getDist())