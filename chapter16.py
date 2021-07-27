from sys import argv

script, filename = argv

print(f"We are going to erase file {filename}")
print(f"If you care about the file {filename}, press ctrl + enter")
print("Else press enter")

input("?")

print("Openeing the file...........")
target = open(filename, 'w')

print("Truncating the file, goodbye....")
target.truncate()

print("Now I am going to ask you to write three lines")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print(f"I am going to write these to file {filename}")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close the file....")
target.close()

print("Check your file for what you typed in")
