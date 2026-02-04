name=input("Enter your name: ")
age=int(input("Enter your age: "))
school1=input("Enter your school: ")
school2=input("Enter your school again: ")
school3=input("Enter your school once more: ")
grade=input("Enter your grade: ")
if grade=="A" or grade=="a" and age>=18:
    print(f"you are going to {school2}")
elif grade=="B" or grade=="b" and age!=18:
    print(f"you are going to {school3}")
elif grade=="C" or grade=="c":
    print(f"you are going to {school1}")
else:
    print("you are not going to any school")