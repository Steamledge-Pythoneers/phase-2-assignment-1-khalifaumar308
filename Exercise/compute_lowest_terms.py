## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
    x=x.split('/')
    n=int(x[0])
    d=int(x[1])
    sign=''
    if n<0 or d<0:
        sign='-'
    n=(n**2)**0.5
    d=(d**2)**0.5
    if d>n:
        if d%n==0:
            return '{}1/{}'.format(sign,int(d/n))
        else:
            while True:
                if n%2==0 and d%2==0:
                    n=n/2
                    d=d/2
                else:
                    return '{}{}/{}'.format(sign,int(n),int(d))
    if n>d:
       if n%d==0:
         return '{}{}/1'.format(sign,int(n/d))
       else:
            while True:
                s=3
                if n%s==0 and d%s==0:
                    n=n/s
                    d=d/s
                        
                else:
                    return '{}{}/{}'.format(sign,int(d),int(n))
                
print(lowest_terms('-50/25'))
