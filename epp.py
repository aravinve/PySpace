i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")

j =1
while j <= 5:
    print('*' * j)
    j += 1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!!")
        break
else:
    print("You Lost!!")

command = ""
launched = False
while True:
    command = input("> ").lower()
    if command == "launch":
        if launched:
            print("Launched Already :[")
        else:
            launched = True
            print("Rocket launched!")
    elif command == "abort":
        if not launched:
            print("Its already aborted!")
        else:
            launched = False
            print("Rocket Aborted!")
    elif command == "help":
        print(""" 
launch: Launch the Rocket
abort: Abort the Rocket
quit: Quit the Command Center
        """)
    elif command == "quit":
        break
    else:
        print("Invalid Command!")