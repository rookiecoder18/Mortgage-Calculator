def mortgage_term():
    while True:
        try:
            amount=float(input('enter the amount you want: '.title()))
            interest=float(input('enter interest rate: '.title()))
            monthly_pay=float(input('How much you will pay each month? '.title()))
        except ValueError:
            print('Error!! Please type only integer or float.')
        else:
            return amount,interest,monthly_pay