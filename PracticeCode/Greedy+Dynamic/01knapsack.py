n = int(input("Enter number of items to be Considered: "))
sackCapacity = int(input("Enter the max Capacity of the Sack: "))
itemWeights = []
itemValues = []
for i in range(1, n+1):
    uw = int(input(f"Enter the weight of Item {i}: "))
    itemWeights.append(uw)
    uv = int(input(f"Enter the value of Item {i}: "))
    itemValues.append(uv)

# Define the KnapSack Function
def knapSack(SC, n, wts, vals):
    # No point in checking if n or sackCap is 0
    if (n == 0) or (SC == 0):
        return 0
    # Perform knapSack Function recursively
    if (wts[n-1] > SC):
        return knapSack(SC, n-1, wts, vals)
    else:
        # Compare Between Sack Values and Item Values
        return max((vals[n-1]+knapSack(SC-wts[n-1], n-1, wts, vals)), knapSack(SC, n-1, wts, vals))
    
# Returning the Max Profit user can get from the Given Items
print(knapSack(sackCapacity, n, itemWeights, itemValues))