from sys import argv
script, user_name = argv

prompt = "$"

print(f"Hi {user_name}, I am (script) script.")
print(f"I would like to ask a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have {user_name}?")
computer = input(prompt)

print(f"""OK, so you said {likes} liking about me
you live in {lives} and you have a {computer} computer,
which is very nice""")
