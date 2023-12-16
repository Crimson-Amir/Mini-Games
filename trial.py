
variable = 0


def hello():
    global variable
    variable = 1

print(variable)
hello()
print(variable)