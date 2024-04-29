# sort_numbers.py
#
# This script reads an integer n from input, then reads n more integers,
# stores them in a list, sorts the list, and prints each number in ascending order.
#
# Input:
# - n : the number of integers that will be read (integer)
# - n integers : numbers to be sorted
#
# Output:
# - Numbers printed one per line in ascending order
#
# Example:
# Input:
# 5
# 5
# 2
# 3
# 4
# 1
# Output:
# 1
# 2
# 3
# 4
# 5

def print_num(numbers):
    for number in numbers:
        print(number)

n = int(input())
numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)
numbers.sort()

print_num(numbers)
