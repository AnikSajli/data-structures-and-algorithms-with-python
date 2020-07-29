def linear_search(elementList, searchItem):
    for i in range(len(elementList)):
        if searchItem == elementList[i]:
            return i;
    i = -1
    return i

result = linear_search([2,3,4], 5)
if result == -1:
    print("Element not found")
else:
    print("Found element at index: ",result)
