def binary_search (list, item):
    low = 0
    hight = len(list) - 1
    a = 0

    while low <= hight:
        a += 1
        mid = int((low + hight)/2)
        guess = list[mid]
        if guess == item:
            return mid, a
        if guess > item:
            hight = mid - 1
        else:
            low = mid + 1
    return None

my_list = list(range(0,100,2))
#print (my_list)
print(binary_search(my_list, 3))
print(binary_search(my_list, 98))