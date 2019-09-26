def greet_user():
    print("Hi There!")
    print("Welcome Aboard")


def greet_user_special(name):
    print("Hi " + name)


def greet_user_full(f_name,l_name):
    print("Hi " + f_name + " " +  l_name)


def sqaure(number):
    return number * number


# Default Return Value is None
def cube(number):
    print(number * number * number)


print("Start")
greet_user()
print("Finish")

greet_user_special("Aravind")
greet_user_special("Rocker")

greet_user_full("Aravind","Venkat")
greet_user_full("Venkat","Aravind")
greet_user_full(l_name="Venkat",f_name="Aravind")

print(sqaure(5))

print(cube(5)) # This actually prints None

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)" : "😊",
        ":(" : "😥"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
result = emoji_converter(message=message)
print(result)