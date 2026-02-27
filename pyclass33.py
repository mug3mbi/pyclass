greetings=["hi,hello,goodmorning"]
while True:
    userinput=input("type your request")
    for userinput in greetings:
        if userinput in greetings:
            print("hi how can i help you")
            break
        else:
            print("wrong input")
    
    
    
if userinput=="quit":
    print("try again later")
    break
        