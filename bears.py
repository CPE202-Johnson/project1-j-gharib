def bears(n):
    print("Execute for ", n)
    #Throw an error for invalid inputs
    if n == None or n < 0:
        raise ValueError

    #Base cases
    if n == 42:
        return True
    elif n < 42:
        return False
    
    
    #Check what happens if you follow the divide by 2 rule
    if(n%2 == 0):
        if bears(int(n/2)):
            return True
        
    #Check if you subtract the last two digits what happens
    if(n%3 == 0):
        #Combine the last 2 digits of the number
        firstNum = n%10
        secondNum = n%100 - n%10
        secondNum /= 10
        res = firstNum * secondNum

        if (res == 0):
            return False
        elif bears(n - res):
            return True

    #Check if you subtract the last two digits what happens
    if(n%4 == 0):
        #Combine the last 2 digits of the number
        firstNum = n%10
        secondNum = n%100 - n%10
        secondNum /= 10
        res = firstNum * secondNum

        if (res == 0):
            return False
        elif bears(n - res):
            return True
    #Check if you subtract 42 what happens
    if (n%5 ==0):
        if bears(n-42):
            return True

    return False

print(bears(210))