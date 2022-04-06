'''l = eval(input('Enter a list of integers'))
l =list(l)'''
lst = [0,1,-5,2,3,3,9,6]
nth = lst[0]
for num in lst:
    index = lst.index(num)
    nth = num
    if num < nth:
        lst.pop(index)
        lst.insert(0,num)
print(lst)


