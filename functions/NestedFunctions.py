'''
def outer_function(outer_var):
    print("I am in outer function : ",outer_var)

outer_function("something")
'''

'''
def outer_function(outer_var):
    print("I am in outer function : ", outer_var)

    def inner_function():
        print("I am in inner function : ",outer_var)
    inner_function()

outer_function("something")
'''
'''
def outer_function(var):
    print("I am in outer function : ", var)

    def inner_function():
        var = "Inner_something"
        print("I am in inner function : ",var)
    inner_function()

outer_function("something")
'''
'''
def outer_function(var):
    print("I am in outer function : ", var)

    def inner_function():
        var = "Inner_something"
        print("I am in inner function : ",var)
    inner_function()
    print("I am in outer function 2 : ", var)

outer_function("something")
'''


def outer_function(var):
    print("I am in outer function : ", var)

    def inner_function():
        nonlocal var
        var = "Inner_something"
        print("I am in inner function : ",var)
    inner_function()
    print("I am in outer function 2 : ", var)


outer_function("something")




