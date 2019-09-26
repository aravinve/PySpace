for item in 'Python':
    print(item)

for item in ["Aravind","Deepika"]:
    print(item)

for i in [1,2,3,4,5]:
    print(i)

for i in range(10):
    print(i)

for i in range(100,110):
    print(i)

for i in range(200,210,3):
    print(i)

prices = [10,20,30]
sum = 0
for price in prices:
    sum += price
print(f"Total Price is: {sum}")


for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

numbers = [5,2,5,2,2]
for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)