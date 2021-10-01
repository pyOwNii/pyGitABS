# This program says hello and asks my name.

print('Hello World')

print('What is your name?') #asks name
myName = input()
print('hello: ' + myName)
print('The length of your name is: ')
print(len(myName))


print('What is your age?' )
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')