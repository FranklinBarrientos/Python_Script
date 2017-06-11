balance=4213
annualInterestRate=0.2
monthlyPaymentRate=0.04
Total_paid=0
print('balance =' + ' '+str(balance))
print('annualInterestRate =' + ' '+str(annualInterestRate))
print('monthlyPaymentRate =' + ' '+str(monthlyPaymentRate))
print

print 'Result Your Code Should Generate:'
print
print'-------------------'

for i in range(1,13):
    
    print('Month: '+ str(i))
    monthlyPay=balance*monthlyPaymentRate
    Total_paid+=monthlyPay
    print('Minimum monthly payment: ' + str(round(monthlyPay,2)))
    RemainBalance=balance-monthlyPay
    balance=RemainBalance+(annualInterestRate/12.0)*RemainBalance
    print('Remaining balance: ' + str(round(balance,2)))    
    
    
    
print('Total paid: ' + str(round(Total_paid,2))) 
print('Remaining balance: ' + str(round(balance,2)))    
