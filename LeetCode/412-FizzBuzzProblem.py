# Let User input any Number
n = int(input("Enter any Number: "))

def fizzBuzz(n):
    res = []
    for i in range(1, n+1):
        # If i is divisible by 3 and 5: You need to add "FizzBuzz" to a List
        if ((i%3 == 0) and (i%5 == 0)):
            res.append("FizzBuzz")

        # If i is divisible by 3: You need to add "Fizz" to a List
        elif (i%3 == 0):
            res.append("Fizz")
        
        # If i is divisible by 5: You need to add "Buzz" to a List
        elif (i%5 == 0):
            res.append("Buzz")
        
        # If i is neither divisible by 3 or 5: You need to add i to the List
        else:
            res.append(str(i))
    return res

print(fizzBuzz(n))