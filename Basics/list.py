numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 76, 93, 58, 25]

maxNum = numbers[0]
for num in numbers:
    if num > maxNum:
        maxNum = num
print(maxNum)

# List Methods
number2 = [1, 3, 4, 6, 7, 8, 7, 3, 6]
print(f"Original list: {number2}")

number2.sort()
print(f"Sorted list: {number2}")

for num in number2:
    if number2.count(num) > 1:
        number2.remove(num)
print(f"Non-duplicate list: {number2}")


