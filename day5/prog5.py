def twoWaySort(arr, n):

    for i in range(0, n):


        if (arr[i] & 1):
            arr[i] *= -1


    arr.sort()


    for i in range(0, n):
        if (arr[i] & 1):
            arr[i] *= -1



arr = [1, 3, 2, 7, 5, 4]
n = len(arr)
twoWaySort(arr, n);
for i in range(0, n):
    print(arr[i], end=" ")
