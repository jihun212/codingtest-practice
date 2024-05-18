for test_case in range(1, 11):
    num = int(input())  # 건물 수 입력받기
    arr = list(map(int, input().split()))  # 건물의 높이 입력받기
    count_view = 0  # 조망권이 확보된 건물 수 초기화
    for i in range(2, len(arr) - 2):  # 배열의 인덱스 에러를 방지하기 위해 3번째 요소부터 시작
        current_high = arr[i]  # 현재 건물의 높이
        highest_high = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])  # 주변 건물 중 가장 높은 건물의 높이

        if current_high - highest_high >= 0:  # 현재 건물이 주변 건물보다 높거나 같으면
            count_view += (current_high - highest_high)  # 조망권이 확보된 차이만큼 더하기
    print("#{} {}".format(test_case, count_view))  # 테스트 케이스별 결과 출력
