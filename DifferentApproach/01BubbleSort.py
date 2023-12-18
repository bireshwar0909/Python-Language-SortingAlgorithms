# Code that will perform bubble sort

arr = [1, 3, 6, 2, 9, 5]

lastUnsortedIndex = len(arr)-1


def swap(myList, num1, num2):
    temp = myList[num1]
    myList[num1] = myList[num2]
    myList[num2] = temp


for i in range(lastUnsortedIndex, 0, -1):
    for i in range(0, lastUnsortedIndex, 1):
        if (arr[i] > arr[i+1]):
            swap(arr, i, i+1)


print(arr)
