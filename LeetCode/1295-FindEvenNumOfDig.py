nums_length = int(input("Enter the Total Number of Elements: "))
nums = []

for i in range(1, nums_length+1):
    nums.append(int(input(f"Enter {i} Element: ")))

count = 0
for num in nums:
    # Ignore numbers less than 0
    if num > 0:
        # Reset digCount for each new number
        digCount = 0
        temp = num
        # Keep incrementing until num = 0
        while (num != 0):
            num //= 10
            digCount += 1
        # Print the number and its digit count
        print(f"Number: {temp}, Digit Count: {digCount}")
        if digCount % 2 == 0:
            count += 1
    else:
        continue

print(count)