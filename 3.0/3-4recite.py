# 첫째 줄 입력
total = int(input("총 금액을 입력하세요 (1 ≤ X ≤ 1,000,000,000): "))
if not (1 <= total <= 1000000000):
    print("입력 범위를 벗어났습니다.")
    exit()

# 둘째 줄 입력
num_of_items = int(input("물건의 종류 수를 입력하세요 (1 ≤ N ≤ 100): "))
if not (1 <= num_of_items <= 100):
    print("입력 범위를 벗어났습니다.")
    exit()

# 물건 정보 입력 및 처리
items = []
for _ in range(num_of_items):
    price, quantity = map(int, input("물건의 가격과 개수를 입력하세요 (1 ≤ a ≤ 1,000,000, 1 ≤ b ≤ 10): ").split())
    if not (1 <= price <= 1000000 and 1 <= quantity <= 10):
        print("입력 범위를 벗어났습니다.")
        exit()
    items.append((price, quantity))

# 계산한 총 금액 구하기
calculated_total = sum(price * quantity for price, quantity in items)

# 결과 출력
if calculated_total == total:
    print("Yes")
else:
    print("No")