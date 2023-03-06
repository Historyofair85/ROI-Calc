print('Bigger Pockets')
income = float(input('Enter Income'))
additional = float(income('Enter additional income'))

total_income = income + additional
print('-Total income will be '+ str(total_income))
print("Now we will get some expenses")

def gather_expenses():
    housing = float(input('Enter you monthly income: '))
    utilities = float(input('Enter utilites: '))
    food = float(input("Enter food expense: "))
    misc = float(input("Enter additional: "))
    total_expenses = housing +  utilities + food + misc
    return total_expenses

expense_total = gather_expenses()
print("Total expenses next month will be $"+ s.tr(expense_total)) 
margin =  total_income - expense_total
if margin >= 0:
    print('Surplus total will be $' +str(margin))
else:
    print('you will come up $' +str(margin) + ' negative!')

print('Thanks for using the monthly budget tool')

    