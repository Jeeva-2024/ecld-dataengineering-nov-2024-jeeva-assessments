def caring(lst):
    smallest=min(lst)
    smallest_index=lst.index(smallest)
    lst1=[]
    sum_diff=0

    for num in lst:
        if num!=smallest:
            reduced_amount=num*0.25
            lst1.append(num-reduced_amount)
            sum_diff+=reduced_amount
        else:
            lst1.append(num)
    lst1[smallest_index]+=sum_diff
    return lst1

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
result=caring(numbers)
print(result)


