def selectionSort(elementList):
    n = len(elementList)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if elementList[j] < elementList[minIndex]:
                minIndex = j

        if minIndex != i:
            temp = elementList[i]
            elementList[i] = elementList[minIndex]
            elementList[minIndex] = temp

    return elementList

sortedList = selectionSort([3,1,8,6])
print(sortedList)
