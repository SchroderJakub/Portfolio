my_list = [10, 5, 20, 15, 8]

largest_number = my_list[0]

for number in my_list:
    if number > largest_number:
        largest_number = number

print("Largest number is:", largest_number)
