lst=[]
number=int(input("Enter the length of the list"))

for i in range(number):
    lst.append(int(input("Enter the number")))

lstmx=[]
theshmaxx2=[]
for i in range(len(lst)):
    lstmx.append(0)
    theshmaxx2.append(0)
sm=0
for i in range(len(lstmx)):
    if (lst[i]>0):
        sm=sm+lst[i]
        for j in range(i+1,len(lstmx)):
            sm=sm+lst[j]
            if (sm>lstmx[i]):
                lstmx[i]=sm
                theshmaxx2[i]=j+1
        sm=0  
maxx=lstmx[0]
for i in range(len(lstmx)):
    if (lstmx[i]>maxx):
        maxx=lstmx[i]
        theshmaxx1=i
upolst=[]

for i in lst[theshmaxx1:theshmaxx2[theshmaxx1]]:
    upolst.append(i)
print (upolst)
   
    
    

