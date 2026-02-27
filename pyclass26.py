total=0
print("coffee(3.50)")
print("tea(2.50)")
print("cookie(1.75)")
print
while True:
    choice=int(input("choose between 1,2,3 to pick an item or 0 to cancel "))

    if choice==0:
        print("thank you and welcome again")
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
        print("0 is the finishing order")

print(total)
