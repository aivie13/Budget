# Aaron Ivie
# Program to recieve user input and output a monthly budget

# recieve user inputs
def inputExpenses():
    print('Please enter the following:')
    income = input("\tYour Monthly Income: $")
    budgetExpenses = input('\tYour Budgeted Expenses: $')
    actualExpenses = input('\tYour Actual Living Expenses: $')
    actualTaxes = input('\tYour Actual Taxes Paid: $')
    actualTithing = input('\tYour Actual Tithe offerings: $')
    other = input('\tAny Other Expenses: $')
    return income, budgetExpenses, actualExpenses, actualTaxes, actualTithing, other

# calculate taxes based on user income
def calculateTaxes(income):
    if income < 9875:
        tax = income* .1
    elif 9875 < income < 40125:
        tax = 987.50 + .12*(income - 9875)
    elif 40125 < income < 85525:
        tax = 4617.5 + .22*(income - 40125)
    elif 85525 < income < 163300:
        tax = 14605.5 + .24*(income - 85525)
    elif 163300 < income < 207350:
        tax = 33271.5 + .32*(income - 163300)
    elif 207350 < income < 518400:
        tax = 47367.5 + .35*(income - 207350)
    else:
        tax = 156253 + .37*(income - 518400)
    return tax

# calculate tithing based on user income
def calculateTithing(income):
    return income / 10.0

def calculateDifference(income, taxes, tithing, living, other):
    return income - (taxes + tithing + living + other)

# display budget chart
def display(income, budgetExpenses, actualExpenses, actualTaxes, actualTithing, other):
    print('\nThe following is a report on your monthly expenses')
    for word in [['Item', 'Budget', 'Actual'], 
    ['===============', '===============', '==============='],
    ['Income', '$' + str('%.2f'%income), '$' + str('%.2f'%income)],
    ['Taxes', '$' + str('%.2f'%calculateTaxes(income)), '$' + str('%.2f'%actualTaxes)],
    ['Tithing', '$' + str('%.2f'%calculateTithing(income)), '$' + str('%.2f'%actualTithing)],
    ['Living', '$' + str('%.2f'%budgetExpenses), '$' + str('%.2f'%actualExpenses)],
    ['Other', '$' + str(0.00), '$' + str('%.2f'%other)],
    ['===============', '===============', '==============='],
    ['Difference', '$' + str('%.2f'%calculateDifference(income, calculateTaxes(income), calculateTithing(income), budgetExpenses, 0.00)),
    '$' + str('%.2f'%calculateDifference(income, actualTaxes, actualTithing, actualExpenses, other))]]:
        print('{:<16} {:<16} {:<16}'.format(*word))


income, budgetExpenses, actualExpenses, actualTaxes, actualTithing, other = inputExpenses()
display(income, budgetExpenses, actualExpenses, actualTaxes, actualTithing, other)
