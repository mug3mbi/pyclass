print("welcome to the system")
print("how is variable initiated\n A.variable:content\n B variable=content\n C variable-content")
while True:
    choice=input("choose between A,B and C").upper()
    if choice=="B":
        print("correct answer")
        break
    elif choice=="A" or choice=="C":
        print("wrong answer try again")
    else : 
        print("wrong input")   


    