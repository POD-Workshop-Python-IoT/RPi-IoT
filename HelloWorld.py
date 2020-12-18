print("Hello World in Python")

print("What is your first name?")
fname = input()
lname = input("What is your last name? ")

if fname != "" and lname != "":
  print("1. Hello " + lname + " " + fname + ", welcome to POD workshop!")
elif fname != "":
  print("No last name entered")
elif lname != "":
  print("No first name entered")
else:
  input("\n Exiting...No first and last name entered!")
  exit()
  
print("2. Hello %s %s, welcome to POD workshop!"%(lname.upper(), fname.upper()) )
print("3. Hello {} {}, welcome to POD workshop!".format(lname.title(), fname.title()) )
print("4. Hello {1} {0}, welcome to POD workshop!".format(fname.swapcase(), lname.swapcase()) )

from Greeting import hello  # import Greeting.py module
# function call to Greeting.py module : hello method
name, count = hello(fname, lname)

# print the returned values
print(name, count)
