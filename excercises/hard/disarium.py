def disarium(n):
    number = n
    lst = []


    while n != 0:
        lst.append(n % 10)
        n = n // 10


    lst.reverse()


    disum = sum(digit ** (index + 1) for index, digit in enumerate(lst))


    return disum == number


print(disarium(135))
