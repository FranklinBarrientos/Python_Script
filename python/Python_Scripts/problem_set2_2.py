balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
MinPay=10

while True:
    update_Balance = balance
    for i in range(1,13):
        Monthly_ub=update_Balance-MinPay
        update_Balance=(monthlyInterestRate+1) * Monthly_ub
        
    if update_Balance < 0:
        break
    else:
        MinPay+=10

print 'Lowest Payment: ' + str(MinPay)