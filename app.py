# chaning an global variable value from global to lacal inside a function.

change_the_world= 'I want to change the world'

def function_change_the_world():
#   to change the value of a global value to a local value inside a function we should use the 
# word global followed by the variable name.
# then in the next line we give a value of the redefined varibale locally.
    global change_the_world
    change_the_world= ' I will change the world'
    return f'Caroline says: {change_the_world}'
print(function_change_the_world())