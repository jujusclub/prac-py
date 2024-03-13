from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

url = f'https://search.naver.com/search.naver?query=강남+날씨'

# 요청을 보냅니다.
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# 날씨 정보 추출
address = soup.find('div', {'class': 'title_area _area_panel'}).find('h2', {'class': 'title'}).text
temperature = soup.find('div', {'class': 'temperature_text'}).text.strip()[5:]
weatherStatus = soup.find('span', {'class': 'weather before_slash'}).text
weatherAir = [info.text.strip() for info in soup.find('ul', {'class': 'today_chart_list'}).find_all('li', {'class': 'item_today'})]
weatherTime = [i.text.strip() for i in soup.find_all('li', {'class': '_li'})]
dailyWeather = [i.text.strip() for i in soup.find_all('ul', {'class': 'week_list'})]

# 응답 메시지 생성
responseBody = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                'simpleText': {
                    'text': f'{address} 현재 온도: {temperature}℃ 날씨: {weatherStatus}'
                }
            },
            {
                'simpleText': {
                    'text': "풀백으로 빠졌습니다!"
                }
            }
        ]
    }
}

print(responseBody)  # 응답 메시지를 콘솔에 출력
