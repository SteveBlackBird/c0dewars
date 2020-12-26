import math

def is_square(n):    
    if n < 0:
        return False
    sqrt = math.sqrt(n)  
    return sqrt.is_integer()

is_square(25)
is_square(-1)
is_square(0)