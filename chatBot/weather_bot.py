from bs4 import BeautifulSoup
import requests

# 사용자로부터 위치를 입력 받습니다.
location = input("날씨를 검색할 위치를 입력하세요: ")

# 입력 받은 위치로 URL을 만듭니다.
url = f'https://search.naver.com/search.naver?query={location}+날씨'

# 요청을 보냅니다.
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# 위치
address = soup.find('div', {'class': 'title_area_area_panel'}).find('h2', {'class': 'title'}).text
print(address)

# 날씨정보
weather_data = soup.find('div', {'class': 'weather_info'})

# 현재온도
temperature = weather_data.find('div', {'class': 'temperature_text'}).text.strip()[5:]
print(temperature)

# 날씨상태
weatherStatus = weather_data.find('span', {'class': 'weather before_slash'}).text
print(weatherStatus)

# 공기상태
weatherAir = soup.find('ul', {'class': 'today_chart_list'})
infos = weatherAir.find_all('li', {'class': 'item_today'})

for info in infos:
    print(info.text.strip())

weatherTime = soup.find_all('li', {'class': '_li'})
for i in weatherTime:
    print(i.text.strip())
    
dailyWeather = soup.find_all('ul',{'class':'week_list'})
for i in dailyWeather:
    print(i.text.strip())
