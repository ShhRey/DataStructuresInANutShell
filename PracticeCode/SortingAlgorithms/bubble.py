elements = []
element_count = int(input("Enter the number of Elements you want to add: "))
for i in range(1, element_count+1):
    elements.append(int(input(f"Enter Element {i}: ")))


def BubbleSort(arr):
    # Traversing through all Elements of Array
    for i in range(len(arr)-1):
        swapped = False
        # Comparing Adjascent Elements
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If List is already sorted, do not Check Further
        if not swapped:
            break
    return arr

print(BubbleSort(elements))