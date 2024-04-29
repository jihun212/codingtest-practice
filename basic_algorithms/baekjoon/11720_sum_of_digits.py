# 11720_sum_of_digits.py
#
# Baekjoon Online Judge problem 11720 (https://www.acmicpc.net/problem/11720)
# 
# Description:
# The program reads an integer n, followed by a number consisting of n digits,
# and outputs the sum of these digits.
#
# Input:
# First line: Integer n, the number of digits in the number (1 <= n <= 100)
# Second line: A number consisting of n digits
#
# Output:
# The sum of the digits of the number

# 숫자의 개수 입력받기
n = int(input())

# 사용자로부터 숫자 문자열 입력받기
number = input()
total_sum = 0  # 자릿수 합을 저장할 변수

# 숫자의 각 자리를 순회하며 합산
for digit in number:
    total_sum += int(digit)  # 문자를 정수로 변환하고 합산

# 계산된 자릿수 합 출력
print(total_sum)
