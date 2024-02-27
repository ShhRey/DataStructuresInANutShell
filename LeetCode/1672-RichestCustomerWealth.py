customer_count = int(input("Enter Number of Customers who's wealth you want to Compare: "))
bank_count = int(input("Enter Number of Bank Accounts for each Customer: "))
accounts = []
for i in range(1, customer_count+1):
    print(f"#======Entering Wealth Details for Customer {i}=======#")
    customer_account = []
    for j in range(1, bank_count+1):
        wealth = int(input(f"Enter Wealth in Bank {j} for Customer {i}: "))
        customer_account.append(wealth)
    accounts.append(customer_account)
print(accounts)

# Function to Calculate Max Wealth of Customer
def maximumWealth(accounts):
    maxWealth = 0
    # Iterate over Every Customer
    for customer in accounts:
        wealth = sum(customer)
        maxWealth = max(maxWealth, wealth)
    return maxWealth

print(maximumWealth(accounts))