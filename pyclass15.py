name=input("enter your name: ")
age=int(input("enter your age: "))
school1=input("enter your school: ")
school2=input("enter your school again: ")
school3=input("enter your school again once more: ")
grade=input("enter your grade: ")
if grade=="A" or grade=="a" and age>=18:
    print(f"you are going to {school2}")
elif grade=="B" or grade=="b" and age!=18:
    print(f"you are going to {school3}")
elif grade=="C" or grade=="c": and age<18:
    print(f"you are going to {school1}")
else:
    print("you are not going to any school")