from pathlib import Path

#Absolute Path
#C:\...\...\...

#Relative Path
#./

path = Path("ecommerce")
print(path.exists())

path = Path("emails")
#print(path.mkdir())
#print(path.rmdir())

for file in path.glob('*.py'):
    print(file)

