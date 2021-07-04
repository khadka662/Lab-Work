#Given three integers, print the smallest one. (Three integers should be user input)

first_integer = int(input('enter the first number:'))
second_integer = int(input('enter the second number:'))
third_integer = int(input('enter the third number:'))

if first_integer < second_integer and first_integer<third_integer :
    print(f'{first_integer} is the smallest one')
elif second_integer< first_integer and second_integer < third_integer:
    print(f'{second_integer} is the smallest one')
else:
    print(f'{third_integer} is the smallest one')