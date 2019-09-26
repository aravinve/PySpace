course = 'Python for beginners'
print(course[0])
print(course[-1])
print(course[-4])

print(course[0:3])
print(course[0:])
print(course[1:])
print(course[:5])

another = course[:]
print(another)

name = 'Aravind'
print(name[1:-1])


first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

lesson = 'Python for beginners'
print(len(lesson))
print(lesson.upper())
print(lesson.lower())
print(lesson)

print(lesson.find('o'))
print(lesson.find('O'))
print(lesson.find('beginners'))
print(lesson.replace('beginners', 'Absolute Beginners'))
print(lesson.replace('P','J'))

print('Python' in lesson)