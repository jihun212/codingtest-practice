# 1546_new_average.py
#
# Baekjoon Online Judge problem 1546 (https://www.acmicpc.net/problem/1546)
#
# Description:
# The program reads an integer n and then reads n scores. It then recalculates the scores by
# transforming each score to a value based on the highest score (score/max_score * 100).
# Finally, it calculates the new average of these transformed scores.
#
# Input:
# First line: Integer n, the number of scores (1 <= n <= 1000)
# Second line: n scores, separated by spaces (each score is a non-negative integer <= 100)
#
# Output:
# The new average of the transformed scores, printed as a float

n = int(input())  # 점수의 개수 입력받기

# 점수 입력받기 및 정수 변환
scores = list(map(int, input().split()))

# 최대 점수 한 번만 계산
max_score = max(scores)

# 재조정된 점수 계산
adjusted_scores = [(score / max_score * 100) for score in scores]

# 새 평균 계산
new_average = sum(adjusted_scores) / len(adjusted_scores)

# 새 평균 출력
print(new_average)
