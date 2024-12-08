
def sort(arr, first, middle, end):

    left = first
    right = middle + 1

    size1 = middle - first + 1
    size2 = end - right +1
    
    if size1 == 1 and size2 == 1:
        #print("{},{}".format(arr[left], arr[right]))
        if arr[left] > arr[right]:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
        return


    temp = []
    while size1 > 0 and size2 > 0:
        
        if arr[left] < arr[right] or arr[left] == arr[right]:
            temp.append(arr[left])
            left += 1
            size1 -= 1

        if arr[right] < arr[left]:
            temp.append(arr[right])
            right += 1
            size2 -= 1 
        
    if size1 > 0:
        while size1 > 0:
            temp.append(arr[left])
            left += 1
            size1 -= 1
        

    if size2 > 0:
        while size2 > 0:
            temp.append(arr[right])
            right += 1
            size2 -= 1
        

    for i in temp:
        arr[first] = i
        first += 1


def printArr(arr):
    print("Printing arr: ")
    for i in arr:
        print(i)

    print()
        
def mergeSort(arr, start, end):
    middle = int(start + ((end - start) / 2))
    
    if start < end:
        mergeSort(arr, start, middle)
        mergeSort(arr, middle + 1, end)

        sort(arr, start, middle, end)


arr = [3,1,2,5,8,4,1,2,10,22,8,10]

mergeSort(arr, 0, len(arr)-1)

printArr(arr)
