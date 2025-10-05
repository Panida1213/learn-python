#โปรแกรมหาผลรวมของจำนวนแบบไม่จำกัดจำนวน โดยใช้ Whileloop กับ Break
total=0
while True:
    number = int(input("ป้อนตัวเลข:"))
    if number<=0: #ทำให้โปรแกรมหยุดการทำงานโดยกำหนดใฟ้ถ้าป้อน 0 หรือจำนวน - จะให้โปรแกรมคำนวณผลรวม
        break
    total+=number
print("ผลรวม = ",total)