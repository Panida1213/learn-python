#ทดสอบเขียน Nested if
username=input("Yourname:")
password=input("Password:")

if username=="member" and password=="1234": #if main
    print("Login successful")
    service=input("Enter service number (1-2):")
    if service=="1":
        print("Withdraw")
    elif service=="2":
        print("Deposit")
    else:
        print("Invalid service number")    
else:
    print("Account not found")