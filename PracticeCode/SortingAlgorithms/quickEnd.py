elements = []
element_count = int(input("Enter the number of Elements you want to add: "))
for i in range(1, element_count+1):
    elements.append(int(input(f"Enter Element {i}: ")))

# Function for defining Partitions
def partition(arr, start, end):
    # Consider Pivot to be the Last Element
    pivot = arr[end]
    pivot_index = start
    # Iterate through every element of list
    for i in range(start, end):
        # Find element smaller than pivot
        if arr[i] <= pivot:
            # Swap Pivot with Smaller Element
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    
    # For Elements bigger than Pivot, swap them with Pivot
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return pivot_index
        
# Recursively call QS Function and create partitions
def QuickSort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        QuickSort(arr, start, pivot_index-1)
        QuickSort(arr, pivot_index+1, end)

QuickSort(elements, 0, len(elements)-1)
print(elements)