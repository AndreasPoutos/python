def sumIntervals(lista):
        lst=[]
        
       
        summ=0
        for i in lista :
                for j in range(i[0],i[1]):
                        lst.append(j)
        print (lst)
        for i in range(0,len(lst)):
                for j in range(i,len(lst)):
                        if (i!=j):
                                if (lst[i]==lst[j]):
                                        summ=summ+1
                        
                        
     
             
        x=len(lst)-summ
        
        print (x)
lista= [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]]
sumIntervals(lista)


