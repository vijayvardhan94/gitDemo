def calc(a,b):
    sum = a + b
    difference = a - b
    product = a * b
    division = a / b
    print(sum, difference, product, division)
    list1 = [sum, difference, product, division]
    listsum = 0
    for i in range(len(list1)):
        listsum += list1[i]
    
    print(list1)
    print(listsum)

calc(3,4)
