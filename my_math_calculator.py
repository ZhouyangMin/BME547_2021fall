# my math calculator
def sqrt(n):
    # we are using n itself as initial approximation, This can definitely be improved

    if n <= 0:
        raise ValueError("sqrt cannot receive a negative number. you sent {}".format(n))
    x = n
    y = 1

    # e decide the accuracy level

    e = 0.000000001
    while(x - y > e):
        x = (x + y)/2
        y = n / x
    return x
    
    
def add_positive_integer(a, b):
    if a < 0 or b < 0:
        raise ValueError("Cannot add negative numbers")
    if type(a) is not int or type(b) is not int:
        raise TypeError("Cannot add non_integers")
    return a + b
    
