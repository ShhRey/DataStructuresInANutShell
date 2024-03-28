# Enter the Length of Array
arr_capacity = int(input("Enter the max capacity of Array: "))

# Initialize a blank array and append elements for comparison
nums = []
for i in range(1, arr_capacity+1):
    element = int(input(f"Enter {i} element of Array: "))
    nums.append(element)

max_count = 0
count = 0

# Iterate through every element of Array
for num in nums:
    if num == 1:
        count += 1
        # Save the Max Occurrences of 1 from the Array
        max_count = max(max_count, count)
    else:
        count = 0

# Return / Print the result
print(max_count)