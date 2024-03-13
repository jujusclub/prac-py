import requests
from bs4 import BeautifulSoup

def get_search_result(query):
    # 구글 검색 결과 페이지 URL
    url = f"https://www.google.com/search?q={query}"

    # HTTP 요청 보내기
    response = requests.get(url)

    # 응답 확인
    if response.status_code == 200:
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 첫 번째 검색 결과의 제목 가져오기
        title_element = soup.find('h3')
        if title_element:
            return title_element.text.strip()
        else:
            return "검색 결과를 찾을 수 없습니다."
    else:
        return "검색에 실패했습니다."

# 사용자에게 검색어 입력 받기
user_query = input("검색어를 입력하세요: ")

# 챗봇으로부터 응답 받기
chatbot_response = get_search_result(user_query)

# 챗봇 응답 출력
print("챗봇: " + chatbot_response)
