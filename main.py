# TIP CALCULATOR

print('--------------------------------------------\n'
      '|              TIP CALCULATOR               |\n'
      '--------------------------------------------')
# the bill after purchase or consumption
bill = float(input('enter the the bill \n'))
# tip, if necessary
tip = int(input('enter tip percentage (2, 5, 10 ...) \n'))

no_of_payers = int(input('enter number of persons to split bill with\n'))
# ppp = pay per person
# we calculate the amount for each person to pay including the tip
ppp = (bill + (bill * tip / 100)) / no_of_payers
# using the format method is quite tricky as it involves various punctuation
tip_bill = '{:.2f}'. format(ppp)
print(f'each person\'s bill is: ${tip_bill}')
