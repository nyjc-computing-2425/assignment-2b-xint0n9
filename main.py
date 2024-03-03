num = input('Enter a number (decimal only): ')
num = num.strip()
dot = num.find(".")
dp = len(num)-dot-1
# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
