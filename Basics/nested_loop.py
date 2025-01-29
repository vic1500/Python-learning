numbers = [5, 2, 5, 2, 2]

for number in numbers:
   print("x" * number)

print('...............')

for number in numbers:
    output = ''
    for i in range(number):
        output += 'x'
    print(output)