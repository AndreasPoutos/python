def prime(n):
    if n==1:
        return False
    for m in range(2,n):
        if n%m==0:
            return False
    return True
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
lista=[a,b]
lst=[]
bol=1
d=int(input("Enter the integer"))
for i in range(lista[0],lista[1]+1):
    lst.append(i)
while bol==1:
    for j in lst:
        for k in range(j+1,lst[-1]):
            if (prime(j)==True&prime(k)==True):
                if abs(k-j)==d:
                    print (j,k)
                    
                    bol=0


