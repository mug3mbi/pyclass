print("Welcome to Python ATM ")
balanceofATM =1000
pin=3561
attempts=0
maximumattempts=3

while attempts<maximumattempts:
    userpin=int(input("enter your pin "))
    if userpin==pin:
        print("accepted pin ")
        break
    else:
        attempts+=1
        print("wrong pin")
        print("attempts remaining",maximumattempts-attempts)
        
if attempts==maximumattempts:
    print("youve been blocked")
else:
    totalwithdrawn=0
    while True:
        print("current balance: ",balanceofATM)
        amount=int(input("write your amount"))
        
        if amount<=0:
            print("enter value of your amount")
        elif amount>balanceofATM:
            print("enter value of invalid amount" )
        else:
            balanceofATM-=amount
            totalwithdrawn+=amount
            print("withdrawn succesful")
            print("balance remaining",balanceofATM)
        if balanceofATM==0:
            print("balance is 0")
            
            
        choise=input("withrdraw again(yes or no)") .lower()
        if choise!="yes":
            break
    print("total withdrawn money",totalwithdrawn)    


            
       


    

    