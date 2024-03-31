nums_length = int(input("Enter the Total Number of Elements: "))
nums = []

for i in range(1, nums_length+1):
    nums.append(int(input(f"Enter {i} Element: ")))

# Consider two pointers
left = 0
right = len(nums)-1
res = []

# Run until right pointer is greater or equal to left pointer
while left <= right:
    # Decrease right pointer
    if abs(nums[left]) < abs(nums[right]):
        res.append(nums[right]**2)
        right -= 1
    # Increase left pointer
    else:
        res.append(nums[left]**2)
        left += 1

# Return New List but in reverse order
print(res[::-1])