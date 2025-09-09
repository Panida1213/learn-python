#long write and Short in 1line same result
A = 3
B = 5 
print(A + B)

#ลองทำเป็นโปรแกรมรับค่าและคำนวณง่ายๆ
num1 = float(input("เงินที่ได้รับ: "))
num2 = float(input("เงินที่ต้องจ่าย: "))

if num1 == num2:
    print("รับมาพอดี",num1 == num2)
elif num1 < num2:
    print("จ่ายตังเพิ่ม",num2 - num1)
else:
    print("เงินทอน",num1 - num2)