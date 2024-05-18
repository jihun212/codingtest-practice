n = int(input())  # 테스트 케이스의 수 입력

for i in range(n):
    input()  # 각 테스트 케이스에서 문자열의 길이 정보 입력받음 (현재 사용하지 않음)
    s = input()  # 문자열 입력
    half_length = len(s) // 2

    # 문자열 길이가 짝수이고, 반으로 나누어 앞부분이 뒷부분과 동일한지 검사
    if len(s) % 2 == 0 and s[:half_length] == s[half_length:]:
        print(f'#{i+1} Yes')
    else:
        print(f'#{i+1} No')
