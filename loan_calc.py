debt = float(input("What is the balance due on the loan?\n"))
apr = float(input("What is the APR on the loan?\n"))
payment = float(input("What will you pay every month on the loan?\n"))
months = int(input("How long should the life of the loan be, in months?\n"))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = debt * monthly_rate
    debt += interest_paid

    if (debt - payment < 0):
            print("The last payment is", debt)
            print("Loan re-paid in", i+1, "months")
            break
    
    debt -= payment

    print("Paid $" + str(payment), "of which $" + str(interest_paid), "was interest")
    print("Now I owe $" + str(debt))

    