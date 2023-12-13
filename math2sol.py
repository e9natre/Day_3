import math
num = int(input())
sqrt_num = int(math.sqrt(num))
print(sqrt_num)

list = []
for x in range(1, sqrt_num+1):
    if num % x == 0:
        list.append(x)
print(list)


list2 = [int(num/x) for x in list]

print(list2)

list3 = (list + list2)

print(list3)

def is_prime(num):
    if num < 2:
        return False
    for i in range (2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True

def solver(numbers):
    numbers.sort(reverse=True)
    for num in numbers:
        if is_prime(num):
            return num
    return None

result = solver(list3)
print(f"The largest prime factor is:{result}")
