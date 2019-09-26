#Lists

names = ["John","Bob","Mosh","Tom","Bane"]
print(names)
print(names[2])
print(names[-1])
print(names[2:])
print(names[2:4])
print(names)
names[0] = 'Jon'
print(names)

nos = [1,25,78,45,12]
max = nos[0]
for i in nos:
    if i > max:
        max = i
print(max)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0])
print(matrix[0][0])
matrix[0][0] = 100
print(matrix[0][0])

for row in matrix:
    for item in row:
        print(item)

numbers = [5,2,1,7,4]
numbers.append(13)
print(numbers)
numbers.insert(0,20)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(2))
print(50 in numbers)
print(numbers.count(2))
numbers.sort()
print(numbers)
numbers.sort()
numbers.reverse()
print(numbers)
numbers_copy =  numbers.copy()
numbers.append(120)
print(numbers)
print(numbers_copy)

numbers.clear()
print(numbers)

tickets = [2,2,4,5,8,7,9,7]
unique_ticket = []

for ticket in tickets:
    if ticket not in unique_ticket:
        unique_ticket.append(ticket)
print(unique_ticket)

#Tuples

tuples = (1,2,3)
# tuples[0] = 9 Cannot modify tuple --> immutable
print(tuples[0])

coordinates = (1,2,3)

#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]

x,y,z = coordinates #Short hand operation --> Tuple Unpacking

print(z)

list_coordinates = [1,2,3]

x,y,z = list_coordinates # List Unpacking

print(z)