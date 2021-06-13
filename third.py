#N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K.
# It should print the two answers for the questions above.

N = int(input("Enter the number of student: "))
K = int(input("Enter the number of apples: "))
distribute = K//N
remaining = K%N
print(f"the number of apple student  gets is{distribute} ")
print(f"the number of apple remains is {remaining}")
