def frequency (text):
    freq = {}
    for char in text.lower():
        freq[char]=freq.get(char,0)+1
    return freq
print(frequency("YOYO HONEY SINGH"))


def reverse(s):
    words = s.split()
    reverse = words[::-1]
    return " ".join(reverse)

print(reverse("HELL WORLD WHAT YOU ARE DOING AI IS EVIL FOR HUMAN"))

L=[1,2,3,4,5,3,4,2,5,6,7,89,99]
L1 =[1,2,3,8,700,99,88,76,4,2,6]

print(list(set(L)  & set(L1) ))


fruits = {"apple": 2, "banana": 3, "cherry": 1}
total_quantity = 0

for fruit, quantity in fruits.items():
    print(fruit, quantity)
    total_quantity += quantity

print("Total:", total_quantity)


my_list = [1, 2, 3, 4, 2, 5, 3, 6, 3]
from collections import Counter

count = Counter(my_list)

duplicates = {item: freq for item, freq in count.items() if freq > 1}
print(duplicates)


n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


def second_largest(nums):
    nums = list(set(nums))  # Remove duplicates
    nums.sort(reverse=True) # Sort descending
    return nums[1] if len(nums) > 1 else None

print(second_largest([10, 20, 40, 30]))
# Output: 30


def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10          # Get last digit
        reversed_num = reversed_num * 10 + digit
        n = n // 10             # Remove last digit
    return reversed_num

print(reverse_number(12345))
# Output: 54321



def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
# Output: [0, 1]
