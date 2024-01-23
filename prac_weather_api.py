# 기상청 API 활용하여 데이터 가져오기 - 시간별
# Python3 샘플 코드 #인증키는 디코딩 사용
import matplotlib.pyplot as plt
import matplotlib as mpl

import requests

##url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'
#params ={'serviceKey' : 'ZrGDYgal64ZqaOH1s7T+Y3PMbNBkUOapuxQnEOLKny38i+mQ6bsMo0a7kXCBUVGNfMIhsMbUwEkK8O6YMKGKfQ==', 
#        'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'dataCd' : 'ASOS', 'dateCd' : 'HR', 'startDt' : '20230101', 
#       'startHh' : '01', 'endDt' : '20240101', 'endHh' : '01', 'stnIds' : '108' }

#response = requests.get(url, params=params)
#print(response.content)

# 기상청 API 활용하여 데이터 가져오기 - 일자별

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
params ={'serviceKey' : 'ZrGDYgal64ZqaOH1s7T+Y3PMbNBkUOapuxQnEOLKny38i+mQ6bsMo0a7kXCBUVGNfMIhsMbUwEkK8O6YMKGKfQ==', 
         'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'dataCd' : 'ASOS', 
         'dateCd' : 'DAY', 'startDt' : '20230101', 'endDt' : '20240101', 'stnIds' : '108' }

response = requests.get(url, params=params)
print(response.content)

# XML 문자열을 ElementTree로 변환
root = ET.fromstring(xml_data)

# 원하는 부분을 출력
for item in root.findall('.//item'):
    tm = item.find('tm').text
    avgTa = item.find('avgTa').text
    minTa = item.find('minTa').text
    maxTa = item.find('maxTa').text
    
    print(f'Time: {tm}, Average Temperature: {avgTa}, 
          Min Temperature: {minTa}, Max Temperature: {maxTa}')