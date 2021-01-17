# int, int -> int
#Recursive function that converts a number to 
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    #base cases
    val = ""
    if(num == None or num < 0 ):
        return ValueError
    elif (num < b):
        if num == 10:
            return "A"
        elif num == 11:
            return "B"
        elif num == 12:
            return "C"
        elif num == 13:
            return "D"
        elif num == 14:
            return "E"
        elif num == 15:
            return "F"
        else: 
            print("I got here")  
            return num

    #Rest of function goes here
    else:
        print("I got here but not There")
        quot = int(num/b)
        val += str(convert(quot, b))
        

    #return val
    return val
print(convert(30,4))