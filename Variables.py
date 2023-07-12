#VARIBLE CASE SENSITIVITY
TEN = 10
ten = 10# TE and ten both are different
print(TEN)


#RESREVED WORDS IN PYTHON
print("Hi Wasim")



print = "Hi Wasim"# Dont ASSIGN reserved words in python as a variable
print(f"Dont use built in func:{print}")


#Following are the reserved words in python:-

#and del from not while
#as elif global or with
#assert else if pass yield
#break except import print
#class exec in raise
#continue finally is return
#def for lambda try

#MULTI ASSIGNMENT VARIABLES

a, b, c, yes = 10, 20, "wasim", True
print(type(a))
print(type(b))
print(type(c))
print(type(yes))

a,A,b,yes = 10, 10.2 , "wasim",True
print(type(a))
print(type(A))
print(type(yes))

#USER INPUT
z = input("Enter the Value of A: ")
t = input("Enter the Value of B: ")
print(f"Sum of z and t is :{z+t}")

name, place, year_of_birth, weight = "Wasim", "Pune", 2002, 62
print(f"""
My name is:{name},
I am from :{place},
My DOB is :{year_of_birth},
My weight is :{weight} in kg""")

# Calculate the age of the user

name = input("Name: ") # always gives you string values
place = input("place: ")
year_of_birth = input("year_of_birth: ")

age = 2023 - int(year_of_birth)

print(f"""
My name is: {name}
I live at: {place}
{name} is of age: {age}
""")
firstname , Lastname , number = "wasimuddin", "syed", "02"
print(f"{firstname}{Lastname}{number}@gmail.com")

# TYPE CONVERSION
#We can convert the data type of one variable into another if it is allowed
A = int(input("Enter value of A: "))
B = int(input("Enter value of B: "))

print(type(A), type(B))

# String to integer
A = "50"
print(f"data type before: {type(A)}, value of A: {A}")
A = int(A)
print(f"data type after: {type(A)}, value of A: {A}")

# float to integer
A = 50.22
print(f"data type before: {type(A)}, value of A: {A}")
A = int(A)
print(f"data type after: {type(A)}, value of A: {A}")

# integer to float
A = 50
print(f"data type before: {type(A)}, value of A: {A}")
A = float(A)
print(f"data type after: {type(A)}, value of A: {A}")

# integer to boolean
A = 10
print(f"data type before: {type(A)}, value of A: {A}")
A = bool(A)
print(f"data type after: {type(A)}, value of A: {A}")

# integer to boolean
A = 0
print(f"data type before: {type(A)}, value of A: {A}")
A = bool(A)
print(f"data type after: {type(A)}, value of A: {A}")

# integer to boolean
A = 1
print(f"data type before: {type(A)}, value of A: {A}")
A = bool(A)
print(f"data type after: {type(A)}, value of A: {A}")

# string to boolean
A = "Sunny"
print(f"data type before: {type(A)}, value of A: {A}")
A = bool(A)
print(f"data type after: {type(A)}, value of A: {A}")

# empty string to boolean
A = ""
print(f"data type before: {type(A)}, value of A: {A}")
A = bool(A)
print(f"data type after: {type(A)}, value of A: {A}")

# MEMORY BLOCK
a = 22
b = 34
c = 22

id(a) # memory address
id(b)


#Memory is assigned to the value of variable passed not the variable name
a = "Sunny"
b = 34
c = "Sunny"

print(id(a), id(b), id(c))

