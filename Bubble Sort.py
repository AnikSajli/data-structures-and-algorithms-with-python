def bubble_sort(elementList):
    for i in range(len(elementList)-1):
        for j in range(len(elementList)-1-i):
            if elementList[j] > elementList[j+1]:
                temp = elementList[j]
                elementList[j] = elementList[j+1]
                elementList[j+1] = temp
    return elementList

sorted_list = bubble_sort([3,4,1,9,0])
print()
