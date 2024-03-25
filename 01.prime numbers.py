n = 10695
is_primenumber = True
for i in range(2, n, 1):
    if n % i == 0:
        is_primenumber = False
        break
if is_primenumber:
    print(n, "is prime number")
else:
    print(n, "is not prime number")