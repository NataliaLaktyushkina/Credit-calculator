import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment', default=False, type=float)
parser.add_argument('--principal', default=False, type=float)
parser.add_argument('--interest', default=False, type=float)
parser.add_argument('--periods', default=False, type=int)
args = parser.parse_args()
if not args.type:
    print('Incorrect parameters')

elif not args.interest:
    print('Incorrect parameters')
#
# if len(args) < 4:
#     print('Incorrect parameters')
else:
    type_payment = args.type

    if type_payment == 'diff':
        if args.payment:
            print('Incorrect parameters')
        else:
            interest = args.interest
            periods = args.periods
            credit_principal = args.principal

            nom_rate = interest / 1200
            total_payment = 0
            for m in range(1, periods + 1):
                d = credit_principal / periods + nom_rate *(credit_principal -
                                                            credit_principal*(m - 1) / periods)
                print(f'Month {m}: paid out {math.ceil(d)}')
                total_payment += math.ceil(d)

            overpayment = total_payment - credit_principal
            print(f'\nOverpayment = {math.ceil(overpayment)}')


    elif type_payment =='annuity':
        if not args.periods:
            credit_principal = args.principal
            monthly_payment = args.payment
            interest = args.interest

            nom_rate = interest / 1200
            months_all = math.log(monthly_payment / (monthly_payment - nom_rate * credit_principal), 1 + nom_rate)
            round_months = math.ceil(months_all)
            years = round_months // 12
            months = round_months % 12
            if months > 0 :
                print(f'You need {years} years and {months} months to repay this credit!')
            else:
                print(f'You need {years} years to repay this credit!')
            overpayment = round_months * monthly_payment - credit_principal
            print(f'\nOverpayment = {math.ceil(overpayment)}')

        elif not args.payment:
            credit_principal = args.principal
            months = args.periods
            interest = args.interest

            nom_rate = interest / 1200
            monthly_payment = credit_principal * nom_rate * pow(1 + nom_rate, months) / (pow(1 + nom_rate, months) - 1)
            monthly_payment = math.ceil(monthly_payment)
            # print(f'credit_principal {credit_principal}  months {months}  interest {interest}')
            print(f'Your annuity payment = {monthly_payment}!' )

            overpayment = months * monthly_payment - credit_principal
            print(f'\nOverpayment = {math.ceil(overpayment)}')

        elif not args.principal:
            monthly_payment = args.payment
            months = args.periods
            interest = args.interest

            nom_rate = interest / 1200
            divisor = nom_rate * pow(1 + nom_rate, months) / (pow(1 + nom_rate, months) - 1)
            credit_principal = monthly_payment / divisor
            credit_principal = round(credit_principal)
            print(f'Your credit principal = {credit_principal}!')
            overpayment = months * monthly_payment - credit_principal
            print(f'\nOverpayment = {math.ceil(overpayment)}')
    else:
        print('Incorrect parameters')


    # calculate_type = input('''What do you want to calculate?
    # type "n" - for count of months,
    # type "a" - for annuity monthly payment,
    # type "p" - for credit principal: ''')
    #
    # if calculate_type == 'n':
    #     credit_principal = float(input('Enter credit principal: '))
    #     monthly_payment = float(input('Enter monthly payment: '))
    #     interest = float(input('Enter credit interest:'))
    #
    #     nom_rate = interest / 1200
    #     months_all = math.log(monthly_payment / (monthly_payment - nom_rate * credit_principal), 1 + nom_rate)
    #     round_months = math.ceil(months_all)
    #     years = round_months // 12
    #     months = round_months % 12
    #     print(f'You need {years} years and {months} months to repay this credit!')
    #
    # elif calculate_type == 'a':
    #     credit_principal = float(input('Enter credit principal: '))
    #     months = float(input('Enter count of periods:'))
    #     interest = float(input('Enter credit interest:'))
    #
    #     nom_rate = interest / 1200
    #     monthly_payment = credit_principal * nom_rate * pow(1 + nom_rate, months) / (pow(1 + nom_rate, months) - 1)
    #     monthly_payment = math.ceil(monthly_payment)
    #     print(f'Your annuity payment = {monthly_payment}!')
    #
    # elif calculate_type == 'p':
    #     monthly_payment = float(input('Enter monthly payment: '))
    #     months = float(input('Enter count of periods:'))
    #     interest = float(input('Enter credit interest:'))
    #
    #     nom_rate = interest / 1200
    #     divisor = nom_rate * pow(1 + nom_rate, months) / (pow(1 + nom_rate, months) - 1)
    #     credit_principal = monthly_payment / divisor
    #     credit_principal = math.ceil(credit_principal)
    #     print(credit_principal)
