
'''
 If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.
'''

temperature = int(input('enter the temperature:'))
if temperature > 30 :
    print(f'it is a hot day')
elif temperature< 10:
    print(f"it is a cold day")
else:
    print(f'it is neither hot or nor cold')