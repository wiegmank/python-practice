total = 0
expenses = []
num_expenses = int(input("How many expenses need to be recorded?\n"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)
print("The total is", total)