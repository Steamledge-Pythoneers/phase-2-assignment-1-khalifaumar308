## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
    """A function that accepts a fraction as input,
    compute and returns the lowest 
    possible form of the fraction"""
    x = x.split('/')#split x into a list
    numerator = int(x[0])#assign n as the numerator
    denomenator = int(x[1])#assign d as the denomerator
    sign = ''#assign an empty string as the defult sign
    if numerator < 0 and denomenator <0:#check if both n and d are negative
        sign = ''
    elif numerator < 0 or denomenator <0:#check if either n or d is negative
        sign = '-'    
    if numerator == 0:#assert that no ZeroDivisionError
        return '0'
    if denomenator == 0:#assert that no ZeroDivisionError
        return 'Undefined'    
    numerator = (numerator**2)**0.5#make n positive
    denomenator = (denomenator**2)**0.5
    #assign the values of n and d to x/y to find hcf
    x = numerator #copy the value of the numerator
    y = denomenator #copy the value of denomenator
    #find the hcf of n and d
    while y != 0:
        i=y
        y=x%y
        x=i
    return '{}{}/{}'.format(sign,int(numerator/x),int(denomenator/x))      

