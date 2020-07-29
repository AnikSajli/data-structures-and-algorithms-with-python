def binary_search(elementList, searchElement):
    n = len(elementList)
    left = 0
    right = n - 1

    while left <= right:
        mid = int ((left+right)/2)
        if elementList[mid] == searchElement:
            return mid
        elif searchElement > elementList[mid]:
            left = mid + 1
        elif searchElement < elementList[mid]:
            right = mid - 1
    return -1

result = binary_search([2,5,9,10],9)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ",result)
