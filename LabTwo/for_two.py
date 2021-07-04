# WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint:
#more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail


marks_math = float(input('enter the marks of math:'))
marks_english = float(input('enter the marks of english:'))
marks_science = float(input('enter the marks of science:'))
marks_computer = float(input('enter the marks of computer:'))
Total_marks = marks_math + marks_english+ marks_science+ marks_computer
percentage = (Total_marks /400)*100
print(f'you got {percentage}%')

if percentage>70  and percentage<=100:
    print(f'congratulation you got distinction')
elif percentage> 60 and percentage<=70:
    print(f'you got first division')
elif percentage>50 and percentage <=60:
    print(f'you got second division')
elif percentage>40 and percentage <=50:
    print(f'you have passed')
elif percentage <40 :
    print(f'you have failed')


