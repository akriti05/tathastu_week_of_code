def intersection(lst1, lst2):
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    return lst3


# Driver Code
lst1 = int(input("enter the list1:"))
lst2 = int(input("enter the list2:"))
print(intersection(lst1, lst2))
