'''If name is less than 3 characters long- name must be at least 3 characters
  otherwise if it's more than 50 characters - name must be maximum of 50 characters
  otherwise - name looks good!
'''

name = str(input('enter the name:'))
if len(name)<3:
    print(f'name must be at least 3 characters')
elif len(name)>50:
    print(f'name must be maximum of 50 characters')
else:
    print(f"name looks good")