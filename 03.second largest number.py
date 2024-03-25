numbers = [4, 5, 3, 7, 8, 2, 1, 6]
largest = max(numbers[0], numbers[1])
second_largest = min(numbers[0], numbers[1])
for number in numbers[2:]:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number
print("Second largest number is:", second_largest)