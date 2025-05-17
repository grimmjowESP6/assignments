students = {'Alice':85,'Arshad':90}
name = input('Enter the student\'s name: ')

#Using in:
print('Using in operation:')
if name in students:
    print("{}'s marks: {}".format(name,students[name]))
else:
    print('Student not found.')

#Using get function:
print('Using get function:')
if students.get(name)==None:
    print(students.get(name,'Student not found.'))
else:
    print("{}'s marks: {}".format(name,students.get(name)))

#using exception handler
print('Using exception handler:')
try:
    print("{}'s marks: {}".format(name,students[name]))
except KeyError:
    print('Student not found.')