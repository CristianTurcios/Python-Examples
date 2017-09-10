def decorator(function):
    def new_function():
        print "Before decorator"
        message = function()
        print (message)
        print "After decorator"
    return new_function

def multiplicate_by_seven(function):
    def before_action():
        print "Firts line to execute in decorator"

    def after_action():
        print "Last line to execute in decorator"

    def multiplicate(*args, **kwargs):
        before_action()
        value = function(*args, **kwargs)
        new_value = value * 7
        print "New value is:", new_value
        after_action()
        return new_value
    return multiplicate

def decorator_with_params(message):
    print "1",  message
    def _decorator(function):
        print "2", message
        def new_function():
            print "3", message
            value = function()
            return value
        return new_function
    return _decorator

@decorator
def init_function():
    return "return print because stored in var"

@multiplicate_by_seven
def sum_numbers(number_one, number_two):
    return number_one + number_two

@decorator_with_params(message = "params in decorator is accesible in all function inside decorator")
def pass_params_to_decorator():
    return "Hello in decorator"


#init_function()
#value = sum_numbers(5, 5)
#print "The final value is:", value
value2 = pass_params_to_decorator()
print  value2
