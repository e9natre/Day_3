import math
num = int(input())
sqrt_num = int(math.sqrt(num))

list = []
for x in range(1, sqrt_num+1):
    if num % x == 0:
        list.append(x)

list2 = [int(num/x) for x in list]

list3 = (list + list2)

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

if __name__ == "main__":
    print(sqrt_num)
    print(list)
    print(list2)
    print(list3)
    result = solver(list3)
    print(f"The largest prime factor is:{result}")
