total=0
print("coffee (3.50)")
print("tea(2.50)")
print("cookie(1.75)")

while True:
    choice=int(input("choose between 1,2,3 to pick between an item or to cancel to 0"))

    if choice==0:
        print("thank you and welcome again ")
        break
    elif choice==1:
        total=total+3.5
        print("3.5 added to your balance")
        print(total)
    elif choice==2:
        total=total+2.5
        print("2.5 added to your balance")
        print(total)
    elif choice==3:
        total=total+1.75
        print("1.75 added to your balance")
        print(total)
    else:
        print("0 is finishing the order")
print(total)
if total==0:
    print("you have not purchased anything")
else:
    tax=total*0.10
    if total>=20:
        discount=total*0.15
        print(total)
    else:
        discount=0
print(total)
finaltotal=total+tax-discount
print(finaltotal)                        


        






