import random
pinakas = [0,1,2,
           3,4,5,
           6,7,8]

def triliza():
    print ('  |   |')
    print (pinakas[0],'|',pinakas[1],'|',pinakas[2])
    print ('----------')
    print (pinakas[3],'|',pinakas[4],'|',pinakas[5])
    print ('----------')
    print (pinakas[6],'|',pinakas[7],'|',pinakas[8])
    print ('  |   |')

def nikh(char,thesh1,thesh2,thesh3):
    if (pinakas[thesh1]==char and pinakas[thesh2]==char and pinakas[thesh3]==char):
        return 1
    
def elegxos(char):
    if (nikh(char,0,1,2)==1):
        return 1
    
    if (nikh(char,3,4,5)):
        return 1
    
    if (nikh(char,6,7,8)):
        return 1
    
    if (nikh(char,0,3,6)):
        return 1
    
    if (nikh(char,1,4,7)):
        return 1
    
    if (nikh(char,2,5,8)):
        return 1
    
    if (nikh(char,0,4,8)):
        return 1
    
    if (nikh(char,2,4,6)):
        return 1
sm=0    
bol=1
triliza()
while (bol==1):
    kinhsh = int(input("Dialekse Thesh"))
    if (sm==5):
        bol=0
    if (pinakas[kinhsh]!= 'x' and pinakas[kinhsh] != 'o'):
        pinakas[kinhsh] = 'x'
        sm=sm+1
        
        if (elegxos("x") == 1):
            print ("Kerdises")
            break;
        while True:
            random.seed()
            upologisths = random.randint(0,8)
            if (pinakas[upologisths]!='o' and pinakas[upologisths]!='x'):
                pinakas[upologisths] = 'o'
                if (elegxos("o") == 1):
                    print ("exases")
                    bol=0
                break;
    
             
             
    else:
        print("dialkse allh thesh")

    triliza()

print ("ksanapaikse")
