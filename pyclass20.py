#welcome
print("create a new account" )
while True :
   username=input("write your username ") .lower()
   password=input("write your password ") 
   age=int(input("write your age "))
   
   if len(password)<6:
       print("password must not be less than 6")
   elif age<13:
        print("you must be older than 13")
   else:
        print("welcome to the website") 
        break 
   
attempts=0
maximumattempts=3
while attempts<maximumattempts :
    loginuser=input("enter your name ") .lower()
    loginpassword=input("eneter your password ")
    
    if loginuser==username  and loginpassword==password:
        print("welcome to the website ",username)
        print("logged in after ",attempts+1) 
        break
    else:
        attempts+=1
print("incorrect login details ")
print("attempts left ",maximumattempts-attempts)

if attempts==maximumattempts:
    print("account locked") 


