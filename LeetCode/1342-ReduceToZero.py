num = int(input("Enter Any Number to Start: "))

# Function for Reducing Number to 0
def numberOfSteps(num: int) -> int:
    stepCounter = 0
    # Run until the Entered Number is not 0
    while num > 0:
        # If num is even, we have to divide by 2 => this will be counted as Step
        if (num%2 == 0):
            print(f"{num} is even => divide by 2")
            num /= 2
            stepCounter += 1
        # If num is odd, we have to subtract by 2 => this will be counted as Step 
        else:
            print(f"{num} is odd => subtract by 1")
            num -= 1
            stepCounter += 1
    return stepCounter

print(f"Number {num} took {numberOfSteps(num)} steps to Reduce to 0")