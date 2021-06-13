# school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
#In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
# The second group has 21 students, so they can get by with no fewer than 11 desks.
#11 desks are also enough for the third group of 22 students. So, we need 32 desks in total. from typing import Any, Union

No_students_class1 = int(input("enter the number of students in class 1:"))
No_students_class2 = int(input("enter the num of students in class 2:"))
No_students_class3 = int(input("enter the number of students in class 3:"))

desk_class1 = (No_students_class1//2)
print(f"required no of desk in class1 is  {desk_class1}")
desk_class2 = (No_students_class2//2)
print(f"required no of desk in class 2 is {desk_class2}")
desk_class3 = (No_students_class3//2)
print(f'required no of desks in class3 is{desk_class3} ')

remain_class1 = (No_students_class1 %2)
print(f'remaining desk for class1 is {remain_class1}')
remain_class2= (No_students_class2 %2)
print(f'remaining desk for class2 is {remain_class2}')
remain_class3= (No_students_class3 %2)
print(f'remaining dsek in class3 is {remain_class3}')
total = desk_class1+desk_class2+desk_class3+remain_class1+remain_class2+remain_class3
print(f"the total no of desk requires is {total}")

