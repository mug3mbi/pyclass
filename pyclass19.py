admin="chris"
password="regie"
loginAdmin=input("write your username ")
loginPassword=input("write your password ")

while admin==loginAdmin.lower() and password==loginPassword.lower():
    print("correct credentials ")
    break
print("try again")