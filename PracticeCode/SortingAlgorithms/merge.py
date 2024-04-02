elements = []
element_count = int(input("Enter the number of Elements you want to add: "))
for i in range(1, element_count+1):
    elements.append(int(input(f"Enter Element {i}: ")))


def MergeSort(arr):
    if len(arr) > 1:
        # First we find the Middle Element of the Main Array and create two Subarrays
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        # Run the MergeSort() function recursively on both Subarrays
        MergeSort(left_arr)
        MergeSort(right_arr)
        
        # Next we compare elements from LA and RA and insert the smaller one first
        i = j = k = 0
        while (i < len(left_arr)) and (j < len(right_arr)):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Check for Remaining Elements in LA
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1  
                  
        # Check for Remaining Elements in RA
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

print(MergeSort(elements))