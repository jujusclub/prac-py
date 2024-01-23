#문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.
# 각 테스트케이스에 대한 입력을 리스트에 저장
testcases = []

# 0 이상 10 미만인 두 정수를 입력받아 테스트케이스 리스트에 추가
while True:
    try:
        A, B = map(int, input().split())
    except ValueError:
        # 입력이 정수가 아닌 경우 예외 처리       
        break

    # 입력 조건 확인 후 테스트케이스 리스트에 추가
    if 0 <= A < 10 and 0 <= B < 10:
        testcases.append((A, B))
    elif A == 0 and B == 0:
        break  # 입력이 0이면 반복문 종료
    else:
        print("0보다 크거나 같고 10 미만의 정수를 입력하세요.")

# 각 테스트케이스에 대한 결과를 리스트에 저장
results = [A + B for A, B in testcases]

# 모든 결과를 출력
# enumerate 함수를 사용하여 인덱스와 값을 함께 얻어와 출력
for  result in results:
    print(result)
