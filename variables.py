# Program to show how variables can be changed in a program in runtime
# in Python and to show how data entry can also be done and the same
# would be printed as is
character_name = "John"
character_age = 35
print("There was a person named " + character_name + ",")
print("His age was ", character_age)
character_name = "Ramadorai"
character_age = 32
print("He changed his name to " + character_name + ".")
print("His age was actually", + character_age)

print("\"Good boy\"")

character_age = int(input("Age:"))
print("His age was actually", + character_age)
print(len(character_name))
