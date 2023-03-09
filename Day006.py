#calculate TIP, using math operators (+,-,/,//,*,**,%)
food_amount= float(input('Enter food amount: '))
tip_percentage= float(input('Enter your tip percentage %: ')) / 100

tip_amount = food_amount * tip_percentage

amount_to_pay= food_amount+tip_amount

print('Actual food bill $',food_amount)
print(f'Tip amount %: ${tip_amount}') #another approach to print dynamic value in string
print('\n')
print('Toatal food bill after tip $'+ str(amount_to_pay)) #another approach to conctenate


