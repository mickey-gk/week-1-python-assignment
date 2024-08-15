#FILE TO GET USER INPUT.
# Instructions:

# Create a new Python file and name it "user_input.py"
# Use the input() function to ask the user for their name and store it in a variable called "name".
# Use the input() function to ask the user for their age and store it in a variable called "age".
# Use the input() function to ask the user for their location and store it in a variable called "location".
# Print out a personalized message u
# sing the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
# Save and run the program to see the output.

name = input("enter your name: ")
age = input("enter your age : ")
location = input("enter your location : ")

print(F"hello! {name}, you are {age} years old and your current location is {location}")

#del all variable and try to print them
del name, age, location
# print( name, age , location)   -prints name, age and location not found.