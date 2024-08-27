import random
b=["-","-","-",
   "-","-","-",
   "-","-","-"]
cP="X"
w=None
gR=True

#printing game board
def printBoard(b) :
    print(b[0]+" | "+b[1]+" | "+b[2])
    print("---------")
    print(b[3]+" | "+b[4]+" | "+b[5])
    print("---------")
    print(b[6]+" | "+b[7]+" | "+b[8])
#player input
def player(b) :
    i=int(input("Enter the position 1-9:"))
    if i>=1 and i<=9 and b[i-1]=="-":
        b[i-1]= cP
    else :
        print ("Spot taken")    
def checkR(b) :
    global w
    if b[0]==b[1]==b[2] and b[0]!="-" :
        w =b[0]
        return True
    elif b[3]==b[4]==b[5] and b[5]!="-" :
        w=b[3]
        return True
    elif b[6]==b[7]==b[8] and b[6]!="-" :
        w=b[6]
        return True
def checkC(b) :
    global w
    if b[0]==b[3]==b[6] and b[0]!="-" :
        w=b[0]
        return True
    elif b[1]==b[4]==b[7] and b[1]!="-" :
        w=b[1]
        return True
    elif b[2]==b[5]==b[8] and b[2]!="-" :
        w=b[2]
        return True
def checkD(b) :
    global w
    if b[0]==b[4]==b[8] and b[0]!="-" :
        w=b[0]
        return True
    elif b[2]==b[4]==b[6] and b[2]!="-" :
        w=b[2]
        return True
def checkW(b) :
    global gR
    if checkD(b) or checkR(b) or checkC(b) == True :
        printBoard(b)
        print(f"The winner is {w}")
        gR=False
def checkT(b) :
    global gR
    if "-" not in b :
        printBoard(b)
        print("Tie")
        gR=False
def switchPlayer() :
    global cP
    if cP=="X" :
        cP= "O"
    else :
        cP="X"
def com(b) :
    while cP=="O" :
        p=random.randint(0,8)
        if b[p] =="-" :
            b[p]= "O"
            switchPlayer()        
s=int(input("Enter 1 player vs player & 2 player vs computer:"))   
if s==1 :
    while gR==True:
        printBoard(b)
        player(b)
        checkW(b)
        checkT(b)
        switchPlayer()
elif s==2 :
    while gR==True:
        printBoard(b)
        player(b)
        checkW(b)
        checkT(b)
        switchPlayer()
        com(b)
        checkW(b)
        checkT(b)
else :
    print("Wrong choice")