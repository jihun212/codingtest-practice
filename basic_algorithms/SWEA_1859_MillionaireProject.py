n = int(input())  # 테스트 케이스의 수 입력

for i in range(n):
    num = int(input())  # 각 테스트 케이스에서의 날짜 수 입력
    arr = list(map(int, input().split()))  # 해당 날짜의 가격 정보 입력
    max_profit = 0
    max_future_price = 0

    # 가격 배열을 역순으로 순회하면서 최대 이익 계산
    for j in range(len(arr) - 1, -1, -1):
        if arr[j] > max_future_price:
            max_future_price = arr[j]
        max_profit += max_future_price - arr[j]

    print(f'#{i+1} {max_profit}')  # 결과 출력
