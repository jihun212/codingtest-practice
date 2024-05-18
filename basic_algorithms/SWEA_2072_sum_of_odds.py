n = int(input())  # 입력받을 테스트 케이스의 수

for i in range(n):
    arr = list(map(int, input().split()))  # 테스트 케이스로 숫자 리스트 입력받기
    total = sum(x for x in arr if x % 2 == 1)  # 홀수인 숫자들의 합 계산
    print(f'#{i+1} {total}')  # 각 테스트 케이스의 결과 출력
