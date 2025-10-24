def divide(a:int,b:int)-> float:
    if b==0:
        raise ZeroDivisionError("Can't divide by zero")
    return a/b

