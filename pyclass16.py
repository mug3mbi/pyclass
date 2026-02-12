#this code is for a calculator
print ("this is my calculator")
num1 =int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")   
num2 =int(input("Enter second number: "))

if operator=="+":
    print("results=",num1+num2)
elif operator=="-":
    print("results=",num1-num2)
elif operator=="/":
    print("results=",num1/num2)
elif operator=="*":
    print("results=",num1*num2)
else:
    print("you have entered the wrong opertor")
    

