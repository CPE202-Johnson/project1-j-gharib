import math
# int, int -> string
#Recursive function that converts a number num to base b
def convert(num, b):
    #base cases
    if(num == None or num < 0 or b == None or b <= 1):
        raise ValueError
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
        return str(num)
    #Rest of function goes here
    else:
        quot = math.trunc(num/b)
        remainder = str(num%b)
        if remainder == "10":
            remainder = "A"
        elif remainder == "11":
            remainder = "B"
        elif remainder == "12":
            remainder = "C"
        elif remainder == "13":
            remainder = "D"
        elif remainder == "14":
            remainder = "E"
        elif remainder == "15":
            remainder = "F"

        return "%s%s" %(convert(quot, b), remainder)
