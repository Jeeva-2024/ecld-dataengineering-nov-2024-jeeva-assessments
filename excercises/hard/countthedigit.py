def count_the_digit(n):

    if n==0:
        return 1
    count = 0
    while n!=0:
        n=n//10
        count = count+1
    return count
print(count_the_digit(45678994737))