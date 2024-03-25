def is_primenumber(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("input number: "))

if is_primenumber(number):
    print(f"{number} is prime number.")
else:
    print(f"{number} is not primenumber.")