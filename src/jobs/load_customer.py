def addition(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b,(int, float)):
        raise TypeError("Input must be either int or float")
    result=a+b
    return result

def substraction(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b,(int, float)):
        raise TypeError("Input must be either int or float")
    result=a-b
    return result

