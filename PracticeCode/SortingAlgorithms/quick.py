elements = []
element_count = int(input("Enter the number of Elements you want to add: "))
for i in range(1, element_count+1):
    elements.append(int(input(f"Enter Element {i}: ")))

# Function for defining Partitions
def partition(arr, start, end):
    # Consider Pivot to be the First Element
    pivot_index = start
    pivot = arr[pivot_index]
    # Keep comparing until start pointer < end pointer
    while start < end:
        # Increment start pointer until element less than pivot found
        while (start < len(arr) and arr[start] <= pivot):
            start += 1
        # Decrement end pointer until element greater than pivot found
        while arr[end] > pivot:
            end -= 1
        # Once desired elements found, swap start and end elements
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    # When start crosses end pointer, swap pivot with end pointer
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return end    
        
# Recursively call QS Function and create partitions
def QuickSort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        QuickSort(arr, start, pivot_index-1)
        QuickSort(arr, pivot_index+1, end)

QuickSort(elements, 0, len(elements)-1)
print(elements)