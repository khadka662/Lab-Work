#9. Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
#Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100

year = int(input('enter the year:'))
if year%4 == 0:
    print(f'LEAP YEAR')
elif year%100 == 0:
    print(f'COMMON YEAR')
else:
    print(f'COMMON YEAR')

