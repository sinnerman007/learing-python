"""
numbers = [2,5,6,8,3,1,9,4,10]
max_number = numbers[0]

for i in numbers:
    if i > max_number:
        max_number = i
print(max_number)

"""


def find_max(numbers):

    max_number = numbers[0]

    for i in numbers:
        if i > max_number:
            max_number = i

    return max_number

