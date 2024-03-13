from bs4 import BeautifulSoup
#텍스트형태의 데이터에서 원하는 html 태그를 추출
import requests


html = requests.get('https://search.naver.com/search.naver?query=서현동+날씨')
# 네이버에 날씨를 검색
#개발자 모드로 들어가서 div 나 class의 이름을 사용 할 것임
soup = BeautifulSoup(html.text,'html.parser') # 크롤링 할 수 있도록 준비

#위치
address = soup.find('div',{'class':'title_area _area_panel'} ).find('h2',{'class':'title'}).text
print(address)

#날씨정보
weather_data = soup.find('div',{'class':'weather_info'} )

#현재온도
#weatherStatus = weather_data.find('span',{'class':'blind'})
temperature = weather_data.find('div',{'class':'temperature_text'}).text.strip()[5:]
#앞 공백제거 strip() 까지만 작성시 현제 온도23.0'
#strip()[5:] 까시 설정시 공백 포함 5글자 삭제됨.
print(temperature)

#날씨상태
weatherStatus = weather_data.find('span', {'class':'weather before_slash'}).text
print(weatherStatus)

#공기상태
weatherAir = soup.find('ul', {'class': 'today_chart_list'})
infos = weatherAir.find_all('li', {'class': 'item_today'})

for info in infos:
    print(info.text.strip())
    
weatherTime = soup.find_all('li',{'class':'_li'})
for i in weatherTime:
    print(i.text.strip())
    
weeklyTitle = soup.find('div',{'class':'weekly_forecast_area _toggle_panel'}).find('h3',{'class':'title'}).text
print(weeklyTitle)
    
dailyWeather = soup.find_all('div',{'class':'day_data'})
for i in dailyWeather:
    print(i.text.strip())
