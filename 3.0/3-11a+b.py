# 각 테스트케이스에 대한 입력을 리스트에 저장
testcases = []

# 0 이상 10 미만인 두 정수를 입력받아 테스트케이스 리스트에 추가
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if 0 <= A < 10 and 0 <= B < 10:
        testcases.append((A, B))
    else:
        print("0보다 크거나 같고 10 미만의 정수를 입력하세요.")

# 각 테스트케이스에 대한 결과를 리스트에 저장
results = [A + B for A, B in testcases]

# 모든 결과를 출력
#enumerate() 함수는 인자의 값을 추출 할 때 인덱스를 추출하는 기법이다. 함수를 사용하면 인덱스 번호와 컬렉션의 원소를 튜플 형태로 반환한다.
#zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받아 동일한 개수로 이루어진 자료형을 묶어서 튜플의 형태로 반환한다.
for i, (result, (A, B)) in enumerate(zip(results, testcases), start=1):
    print("case #{}: {} + {} = {} ".format(i, A, B, result))
