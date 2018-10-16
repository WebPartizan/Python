def binary_search (list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = int((low + hight)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            hight = mid - 1
        else:
            low = mid + 1
    return None

my_list = list(range(0,100))
#print (my_list)
print(binary_search(my_list, 3))
print(binary_search(my_list, 98))