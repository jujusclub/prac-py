# 테스트케이스의 개수 T 입력
T = int(input())

# 각 테스트케이스에 대한 입력을 리스트에 저장
testcases = []
for _ in range(T):  #언더스코어 _는 반복문에서 사용되는 변수의 값이 필요하지 않을 때, 즉 반복 횟수만큼 반복해야 하지만 실제로 변수의 값을 사용하지 않을 때 사용
    A, B = map(int, input().split())  #사용자로부터 공백을 기준으로 구분된 두 개의 정수를 입력받아 변수 A와 B에 할당하는 코드입니다.
    testcases.append((A, B)) #t estcases라는 리스트에 새로운 튜플을 추가하는 코드 A,B는 입력 받은 정수 값

# 각 테스트케이스에 대한 결과를 리스트에 저장
results = [A + B for A, B in testcases]
#for A, B in testcases: testcases 리스트의 각 튜플에서 A와 B를 차례로 추출합니다.
#A + B: 추출된 A와 B를 더합니다.
#[A + B for A, B in testcases]: 위에서 구한 결과들을 리스트로 만듭니다.
#따라서 results 리스트에는 각 테스트케이스의 A와 B를 더한 결과가 저장되게 됩니다.

# 모든 결과를 출력
for result in results:
    print(result)