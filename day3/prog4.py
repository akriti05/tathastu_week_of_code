def duplicate(l):
    copy_list =[]
    for i in l:
        if i not in copy_list:
            copy_list.append(i)

    return copy_list


size= int(input("\nEnter list size:"))
my_list = []
print("\nEnter list elements:")
for  i in range(size):
    elem = input("Element {}:".format(i+1))
    my_list.append(elem)

print("\nNew list:",duplicate(my_list))
