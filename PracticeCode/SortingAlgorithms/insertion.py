elements = []
element_count = int(input("Enter the number of Elements you want to add: "))
for i in range(1, element_count+1):
    elements.append(int(input(f"Enter Element {i}: ")))


def InsertionSort(arr):
    # Traversing through all Elements of Array
    for i in range(1, len(arr)):
        # Defining Pointer to set boundary between Sorted and Unsorted Array
        key = arr[i]
        j = i-1
        # Compare Current Element with Prev and Swap if not Sorted
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        # Return the Pointer back to Original Position
        arr[j+1] = key
    return arr

print(InsertionSort(elements))