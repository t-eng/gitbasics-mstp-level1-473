def add(a,b):
    c=a+b
    print(c)
def prime(n):
    temp=0
    for i in range(1,n+1):
        if(n%i==0):
            temp+=1
    if temp==2:
        return True
    else:
        return False
