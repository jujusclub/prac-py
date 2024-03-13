from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_weather(location):
    url = f'https://search.naver.com/search.naver?query={location}+날씨'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    # 위치
    address_element = soup.find('div', {'class': 'title_area _area_panel'})
    if address_element:
        address = address_element.find('h2', {'class': 'title'}).text
    else:
        address = '위치 정보를 찾을 수 없습니다.'

    # 날씨정보
    weather_data = soup.find('div', {'class': 'weather_info'})

    # 현재온도
    temperature = weather_data.find('div', {'class': 'temperature_text'}).text.strip()[5:]

    # 날씨상태
    weatherStatus = weather_data.find('span', {'class': 'weather before_slash'}).text

    # 공기상태
    weatherAir = soup.find('ul', {'class': 'today_chart_list'})
    air_infos = weatherAir.find_all('li', {'class': 'item_today'})

    air_info_list = [info.text.strip() for info in air_infos]

    # 시간대별 날씨
    weatherTime = soup.find_all('li', {'class': '_li'})
    time_weather_list = [i.text.strip() for i in weatherTime]
    
    # 주간날씨 요약
    weeklyTitle = soup.find('div',{'class':'weekly_forecast_area _toggle_panel'}).find('h3',{'class':'title'}).text
    
    dailyWeather = soup.find_all('div',{'class':'day_data'})
    daily_weather_list = [i.text.strip() for i in dailyWeather]

    return address, temperature, weatherStatus, air_info_list, time_weather_list,weeklyTitle, daily_weather_list

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        address, temperature, weatherStatus, air_info_list, time_weather_list,weeklyTitle, daily_weather_list = get_weather(location)
        return render_template('index.html', address=address, temperature=temperature, weatherStatus=weatherStatus,
                               air_info_list=air_info_list, time_weather_list=time_weather_list,weeklyTitle=weeklyTitle, daily_weather_list=daily_weather_list)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
