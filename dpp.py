is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovely day")
print("Enjoy your day")

loan = 1000
is_good = True
total = 0
if is_good:
    total = (loan * 0.1) + loan
else:
    total = (loan * 0.2) + loan

print(f'Your total loan is ${total}')

has_high_income = True
has_good_credit = True

#And : both True
#Or : atleast one True
#Not : return opp value

if has_high_income and has_good_credit:
    print("Eligible For Loan!")

has_good_credit =  False

if has_good_credit or has_high_income:
    print("Eligible for Loan!")

has_good_credit = True
has_crminal_record = False

if has_good_credit and not has_crminal_record:
    print("Good Boy!")

has_crminal_record = True

if has_good_credit and not has_crminal_record:
    print("Bad Boy!") # Not printed

temperature = 35

# > < >= <= Comparison Operators
if temperature > 30:
    print("Hot Day")
else:
    print("Not a hot day")

user_name = input("Enter user name: ")

if len(user_name) < 5:
    print("Too Short")
elif len(user_name) > 6:
    print("Wrong")
else:
    print("good")

weight = int(input("Enter weight: "))
weight_format = input("(L)bs or (K)g: ")

if weight_format.upper() == 'L':
    sum = weight * 0.4
    print(f"You are {sum} kgs")
elif weight_format.upper() == 'K':
    sum = weight // 0.45
    print(f"You are {sum} pounds")
else:
    print("Wrong Format")