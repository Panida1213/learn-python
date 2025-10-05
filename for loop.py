#ทดสอบเขียน for loop ใช้ในกรณีรู้จำนวนรอบ
for counter in range(1,6,): #ถ้าเขียน(1,6) จะทำ 1-5 
    print(counter)

for counter in range(7): #ถ้าเขียนใน range 7 หมายถึง นับตั้งแต่ 1-6
    print(counter)

for counter in range(2,6): #ถ้าเขียน range 2,6 หมายถึงเริ่มตั้นนับที่ 2 ถึง 5 เพราะ 6 คือหยุดนับ
    print(counter)

for counter in range(10,0,-1): #หมายถึงให้นับลงไปจาก 10 ทีละ -1
    print(counter)

for counter in range(1,10,2):#หมายถึงให้นับเริ่มจาก 1 เพิ่มขึ้นทีละ 2 จนภึง 10
    print(counter)