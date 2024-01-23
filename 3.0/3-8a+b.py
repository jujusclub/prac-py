# 테스트케이스의 개수 T 입력
T = int(input())

# 각 테스트케이스에 대한 입력을 리스트에 저장
testcases = []
for _ in range(T):
    # 사용자로부터 공백을 기준으로 구분된 두 개의 정수를 입력받아 변수 A와 B에 할당하는 코드입니다.
    A, B = map(int, input().split())
    # testcases 리스트에 새로운 튜플을 추가하는 코드로, A와 B는 입력 받은 정수 값입니다.
    testcases.append((A, B))

# 각 테스트케이스에 대한 결과를 리스트에 저장
# for A, B in testcases: testcases 리스트의 각 튜플에서 A와 B를 차례로 추출합니다.
# A + B: 추출된 A와 B를 더합니다.
# [A + B for A, B in testcases]: 위에서 구한 결과들을 리스트로 만듭니다.
# 따라서 results 리스트에는 각 테스트케이스의 A와 B를 더한 결과가 저장되게 됩니다.
results = [(A + B, A, B) for A, B in testcases]

# 모든 결과를 출력
for i, (result, A, B) in enumerate(results, start=1):
    # enumerate(results, start=1)는 1부터 시작하는 인덱스와 함께 results 리스트를 반복합니다.
    # i는 인덱스, result는 results 리스트의 첫 번째 값(A + B의 결과), A와 B는 각각 두 번째와 세 번째 값입니다.
    print("case #{}: {} + {} = {} ".format(i, A, B, result))
    # 출력 문자열을 포맷팅하여 "case #인덱스: A + B = 결과" 형식으로 출력합니다.
