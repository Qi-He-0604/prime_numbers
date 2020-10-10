import math

num_list = []
for i in range(1, 31):
    num_list.append(i)
print(num_list)

prime_list = []
for number in num_list[:]:
    is_prime = True
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(number)
        num_list.remove(number)

print('Prime numbers are: ' + str(prime_list))
print('Non-prime numbers are: ' + str(num_list))



