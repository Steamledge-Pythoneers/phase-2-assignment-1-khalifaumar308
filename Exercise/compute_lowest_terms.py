## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
    x=x.split('/')#split x into a list
    n=int(x[0])#assign n as the numerator
    d=int(x[1])#assign d as the denomerator
    sign=''#assign an empty string as the defult sign
    if n<0 and d<0:#check if both n and d are negative
        sign=''
    elif n<0 or d<0:#check if either n or d is negative
        sign='-'    
    if n==0:#assert that no ZeroDivisionError
        return '0'
    if d==0:#assert that no ZeroDivisionError
        return 'Undefined'    
    n=(n**2)**0.5#make n positive
    d=(d**2)**0.5
    #assign the values of n and d to x/y to find hcf
    x=n
    y=d
    while y!=0:#find the hcf of n and d
        i=y
        y=x%y
        x=i
    return '{}{}/{}'.format(sign,int(n/x),int(d/x))      

