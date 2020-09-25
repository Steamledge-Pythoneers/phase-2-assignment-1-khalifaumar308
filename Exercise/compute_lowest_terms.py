## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
    x=x.split('/')
    n=int(x[0])
    d=int(x[1])
    sign=''
    if n==0:
        return '0'
    if d==0:
        return 'Undefined'    
    if n<0 or d<0:
        sign='-'
    n=(n**2)**0.5
    d=(d**2)**0.5
    x=n
    y=d
    while y!=0:
        i=y
        y=x%y
        x=i
    return '{}{}/{}'.format(sign,int(n/x),int(d/x))      
print(lowest_terms('-12/-26'))
