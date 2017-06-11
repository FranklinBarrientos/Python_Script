balance = 3329
annualInterestRate = 0.2
month = 0
update_Balance = balance
monthlyInterestRate = annualInterestRate/12.0
minPayment = 10

while update_Balance > 0:
    while month < 12:
        month += 1
        update_Balance += (monthlyInterestRate * update_Balance)
        update_Balance -= minPayment
    if  update_Balance <= 0:
        break
    else:
        month = 0
        update_Balance = balance
        minPayment += 10

print('Result Your Code Should Generate:')
print('')
print('-------------------')
print 'Lowest Payment: ' + str(minPayment)