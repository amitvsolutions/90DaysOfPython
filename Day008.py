# functions in python

# function with no argument
def print_my_name():
    print("Hello Amit")

print_my_name()

'''
function with one argument
'''
name = input("Enter your name: ")
# positional arguments
def print_name(name,greet='Hello'):
    print(f'{greet} {name}')

print_name(name,greet='Hi')