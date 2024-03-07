elements = []
element_count = int(input("Enter the number of Elements you want to add: "))
for i in range(1, element_count+1):
    elements.append(int(input(f"Enter Element {i}: ")))


def SelectionSort(arr):
    # Traversing through all Elements of Array
    for i in range(len(arr)-1):
        # Defining Min Index to set boundary between Sorted and Unsorted Array
        min_index = i
        # Find Minimum from Unsorted Array
        for j in range(min_index+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Perform swapping of Desired Elements
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(SelectionSort(elements))