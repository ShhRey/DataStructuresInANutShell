# Random Numbers to be added into the Array
arr_length = int(input("Define Length of Array: "))
nums = []

# Enter Elements of Array
for i in range(0, arr_length):
    nums.append(int(input(f"Enter {i} Element: ")))

# =========================== Customize Code Different from LeetCode =========================== #

# Iterate through Array except 1st
for i in range(1, len(nums)):
    nums[i] += nums[i-1]
print(nums)