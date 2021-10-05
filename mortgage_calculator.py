from mypackage import mortgage_terms
amount,interest,monthly_pay=mortgage_terms.mortgage_term()

daily_interest=(amount*interest/100)/365
month_int=daily_interest*30
print(f'Your monthly interest:Rs {month_int:.2f}')
duration=0
total=amount+month_int

while total>=monthly_pay:
    total-=monthly_pay
    total+=month_int
    #print(f'your due amount Rs.{total:.2f}'.title())
    duration+=1
#print(f'Your mortgage duration would be around {duration} months')

total_amount=amount+month_int*duration
#print(f'You will pay Rs.{total_amount:.2f} in {duration} months.')

print('________________________________________________________________________________')
print('Loan Amount\t|\tDuration\t|\tEMI\t|\tTotal Paid')
print('\t\t|\t\t\t|\t\t|')
print(f'{amount}\t|\t{duration}\t\t|\t{monthly_pay}\t|\t{total_amount:.2f}')
print('\t\t|\t\t\t|\t\t|')
print('________________________________________________________________________________')