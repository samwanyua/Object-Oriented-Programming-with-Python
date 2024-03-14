# Decorators - way to change or modify behavior of functions

'''
** BASISS OF FUNCTIONS ** 
def f1():
    print("Called f1")
f1()

def f2(f):
    f()

f2(f1) # Called f1
'''

def function_one(func):
    def wrapper_function():
        print("Started")
        func()
        print("Ended")

    return wrapper_function

@function_one # same as .... done = function_one(simple_func)
def simple_func():
    print("Getting to understand decorators")

simple_func() # works well (prints 3 lines)

# function_one(simple_func) #prints nothing

# function_one(simple_func()) # Getting to understand decorators

# print(function_one(simple_func)) # <function function_one.<locals>.wrapper_function at 0x7f097a27b0d0>
# function_one(simple_func)() # works well (prints 3 lines)

# function aliasing
# done = function_one(simple_func)
# done()


# args and kwargs
def one(funct):
    def wrapper(*args, **kwargs):
        funct(*args, **kwargs)
    return wrapper

@one
def two(a, b, C = 9043958):
    print(a,b,C)
two("Hi", "George")


# example 3 - returning values from a decorated function
def cool_function(funct):
    def wrapper(*args, **kwargs):
        value = funct(*args, **kwargs)
        return value
    return wrapper

@cool_function
def another_function(a, b =0):
    return a + b

print(another_function(234,3423)) # 3657

# example 4
def before_after(func):
    def wrapper(*args):
        print("Started")
        func(*args)
        print("Ended")

    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print("My function ran")

# instantiate
sample_funct = Test()
sample_funct.decorated_method()


# example 5
import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took: ", time.time() - before, "sec")

    return wrapper

@timer
def run():
    time.sleep(2)

run()