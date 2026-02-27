phone = "0712345678"
pin = "1234"
balance = 0
day = 1

data_mb = 0
data_expiry = 0

while True:
    print()
    print("Day:", day)
    print("1. Deposit Money")
    print("2. Buy Daily Bundle")
    print("3. Check Balance")
    print("4. Next Day")
    print("0. Exit")

    choice = input("Choice: ")

    if choice == "1":
        amount = int(input("Enter amount: "))
        balance = balance + amount
        print("Deposited", amount, ". Balance:", balance)

    elif choice == "2":
        print("1. 100MB @ 20")
        print("2. 500MB @ 50")
        print("3. 1GB @ 100")
        pick = input("Pick: ")
        entered_pin = input("Enter PIN: ")

        if entered_pin != pin:
            print("Wrong PIN. Transaction cancelled.")
        elif pick == "1":
            if balance < 20:
                print("Insufficient balance.")
            else:
                balance = balance - 20
                data_mb = 100
                data_expiry = day + 1
                print("Success! 100MB bought. Expires Day", data_expiry)
        elif pick == "2":
            if balance < 50:
                print("Insufficient balance.")
            else:
                balance = balance - 50
                data_mb = 500
                data_expiry = day + 1
                print("Success! 500MB bought. Expires Day", data_expiry)
        elif pick == "3":
            if balance < 100:
                print("Insufficient balance.")
            else:
                balance = balance - 100
                data_mb = 1024
                data_expiry = day + 1
                print("Success! 1GB bought. Expires Day", data_expiry)
        else:
            print("Invalid option.")

    elif choice == "3":
        print("M-Pesa:", balance)
        if data_mb > 0 and data_expiry > day:
            print("Data:", data_mb, "MB (expires Day", str(data_expiry) + ")")
        else:
            print("Data: 0MB")

    elif choice == "4":
        day = day + 1
        print("Now Day", day)
        if data_expiry != 0 and day >= data_expiry:
            print("Your data has expired!")
            data_mb = 0

    elif choice == "0":
        print("Goodbye")
        break

    else:
        print("Invalid choice. Try again.")