n = int(input("정수를 입력하세요: "))

if not (n % 4 == 0):
    print("입력 범위를 벗어났습니다.")
    exit()

# n을 4로 나눈 몫을 i에 할당
i = n // 4

for _ in range(i):
    print("long", end=" ")
    
    
print("int")

    