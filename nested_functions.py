# In nested functions, if you want to change the value of the outer function's variable inside inner function, then you need to use 'nonlocal' keyword

def count():
    count = 0

    def increment():
        # The 'nonlocal' keyword is used to reference to the variable living outside of this function scope
        nonlocal count
        count += 1
        print(count)

    increment()

count()