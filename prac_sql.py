from bs4 import BeautifulSoup
#텍스트형태의 데이터에서 원하는 html 태그를 추출
import requests
import pymysql


html = requests.get('https://search.naver.com/search.naver?query=강남+날씨')
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
    
    
    
# MySQL 연결 정보 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '0521',
    'database': 'prac_weather',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# MySQL 연결
# cursor클래스는 DB의 sql 구문을 실행시키고 조회된 결과를 가져오게 된다.
connection = pymysql.connect(**db_config)

try:
    with connection.cursor() as cursor:
        # 위치 정보 삽입 예제
        address_sql = "INSERT INTO date_weather (address) VALUES (%s)"
        cursor.execute(address_sql, (address,))

        # 날씨 정보 삽입 예제
        weather_sql = "INSERT INTO date_weather (temperature, weather_status) VALUES (%s, %s)"
        cursor.execute(weather_sql, (temperature, weatherStatus))

        # 공기 상태 정보 삽입 예제
        for info in infos:
            air_sql = "INSERT INTO date_weather (info) VALUES (%s)"
            cursor.execute(air_sql, (info.text.strip(),))

        # 시간대별 날씨 정보 삽입 예제
        for i, time_info in enumerate(weatherTime):
            time_sql = "INSERT INTO date_weather (time, info) VALUES (%s, %s)"
            cursor.execute(time_sql, (i, time_info.text.strip()))

    # 모든 쿼리 실행 후 커밋
    connection.commit()

finally:
    # 연결 닫기
    connection.close()