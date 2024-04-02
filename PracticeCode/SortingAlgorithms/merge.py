elements = []
element_count = int(input("Enter the number of Elements you want to add: "))
for i in range(1, element_count+1):
    elements.append(int(input(f"Enter Element {i}: ")))

# Perform Recursive Function onto SubArrays
def MergeSort(arr):
    if len(arr) > 1:
        # First we find the Middle Element of the Main Array and create two Subarrays
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        # Call Function Recursively
        MergeSort(left_arr)
        MergeSort(right_arr)
        merge(arr, left_arr, right_arr)
    return arr

# Function containing actual logic for merging elements
def merge(arr, left_arr, right_arr):
    i = j = k = 0
    # Compare Elements from Left and Right Arrays simultaneously
    while i < len(left_arr) and j < len(right_arr):
        # If element from left array is small, insert that into arr[k]
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        # If element from right array is small, insert that into arr[k]
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Keep Comapring until all elements from left array are traversed
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Keep Comapring until all elements from right array are traversed
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

print(MergeSort(elements))