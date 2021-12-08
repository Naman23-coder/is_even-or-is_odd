
def is_even(number:int)->bool:
    if number%2==0:
        return True
    else: 
        return False
        
def is_odd(number:int)->bool:
     return not is_even(number)
