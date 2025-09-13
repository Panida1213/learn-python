#ทดสอบเขียน match case
service=input("Enter service number(1-3):")

match service:
    case "1":print("Withdraw")
    case "2":print("Deposit")
    case "3":print("balance")
    case "":print("Invalid service number")