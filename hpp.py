#Dictionaries

customer = {
    "name": "John Smith",
    "age": 20,
    "is_verified": True
}
print(customer["name"])
# print(customer["Nsd"])  -- error occurs
print(customer.get("birthday"))
print(customer.get("birthday", "Jan 1 1990"))
customer["name"] = "Aravind Rocker"
print(customer["name"])

phone = input("Phone: ")

phone_directory = {
    "1" : "One",
    "2" : "Two"
}
out = ""
for c in phone:
    out += phone_directory.get(c,"!") + " "
print(out)

message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "😥"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)