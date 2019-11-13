name = input("What's your name? ")
age = int(input("What's your age? "))

print("Hello " + name + "!")
print("You are " + str(age) + " years old")

if age >= 13 and age <=19:
    print("You are a teen")
elif age < 13:
    print("You are a child")
else:
    print("You are an adult")