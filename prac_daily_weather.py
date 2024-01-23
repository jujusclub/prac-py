from flask import Flask, render_template
import xml.etree.ElementTree as ET
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def weather_data():
    try:
        url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'

        # 현재 날짜를 'YYYYMMDD' 형식의 문자열로 변환
        current_date = datetime.now().strftime('%Y%m%d')
        print("아ㅏ아아아")
        print(current_date)
    
        params = {
            'serviceKey': 'ZrGDYgal64ZqaOH1s7T+Y3PMbNBkUOapuxQnEOLKny38i+mQ6bsMo0a7kXCBUVGNfMIhsMbUwEkK8O6YMKGKfQ==',
            'pageNo': '1',
            'dataType': 'XML',
            'dataCd': 'ASOS',
            'dateCd': 'DAY',
            'startDt': '20230101',
            'endDt': '20240101',  # 현재 날짜로 설정
            'stnIds': '108',
            'numOfRows': '100'
        }

        all_rows = ""  # 모든 페이지의 결과를 저장할 변수

        # 페이지 번호를 1부터 시작하여 계속해서 API 요청을 수행
        page_number = 1
        while True:
            params['pageNo'] = str(page_number)
            response = requests.get(url, params=params)
            response.raise_for_status()  # 요청이 실패하면 예외 발생

            xml_data = response.content

            root = ET.fromstring(xml_data)
            current_page_rows = ""
            for item in root.findall('.//item'):
                tm = item.find('tm').text
                avgTa = item.find('avgTa').text
                minTa = item.find('minTa').text
                maxTa = item.find('maxTa').text
                current_page_rows += f"<tr><td>{tm}</td><td>{avgTa}</td><td>{minTa}</td><td>{maxTa}</td></tr>"

            all_rows += current_page_rows

            # 다음 페이지가 없으면 반복 종료
            if not root.find('.//totalCount').text or int(root.find('.//totalCount').text) <= page_number * int(params['numOfRows']):
                break

            page_number += 1

        return render_template('weather_data.html', table_rows=all_rows)

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False, port=80)
