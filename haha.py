import pymysql
import random
from datetime import datetime, timedelta

# 사용자로부터 메뉴 입력 받기
menu = input("원하는 메뉴를 입력하세요: ")

if menu == '비밀번호':
    # MySQL 연결 설정
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='0521',
        database='doorlock_prac',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # 0부터 9까지의 숫자 중에서 중복을 허용하여 4개의 숫자를 랜덤으로 선택
            random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            print(random_numbers)
            
            # 데이터베이스에 삽입할 쿼리 작성 (id 필드 생략)
            sql = "INSERT INTO random_numbers (random_number, date) VALUES (%s, %s)"
            
            # 현재 시간
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # 쿼리 실행
            cursor.execute(sql, (random_numbers, current_time))
            
            # 변경사항을 커밋
            connection.commit()
                        
            # 현재 시간비밀번
            current_time = datetime.now()
            
            # 5분 전 시간
            five_minutes_ago = current_time - timedelta(minutes=1)
        
            # 5분 전 시간을 문자열로 변환하여 삭제 조건 설정
            delete_condition = five_minutes_ago.strftime('%Y-%m-%d %H:%M:%S')

            # 5분이 지난 레코드 삭제 쿼리 작성
            delete_sql = "DELETE FROM random_numbers WHERE date < %s"

            # 삭제 쿼리 실행
            cursor.execute(delete_sql, (delete_condition,))
            
        
            # 변경사항을 커밋
            connection.commit()
            
    finally:
        # 커서 닫기
        cursor.close()
        # 커넥션 닫기
        connection.close()
else:
    print("다른 메뉴를 선택해주세요.")

