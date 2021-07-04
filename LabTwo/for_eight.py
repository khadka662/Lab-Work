'''
8. Given a three-digit number. Find the sum of its digits.
'''


num = int(input('enter the number:'))
sum = 0
while num>0:
    i = num%10
    sum = sum+i
    num = int(num/10)
print(f"Sum of Digits of Given Number:{sum}")