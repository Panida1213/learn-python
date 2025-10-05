#break คือจะหยุดทำงานในลูป แล้วไปทำงานกับคำสั่งนอกลูปทันที
for counter in range(1,11):
    if counter==5:
        break
    print(counter)
print("จบการทำงาน")

#continue คือ การหยุดการทำงานแล้วย้อนไปเริ่มทำงานใหม่
for counter in range(1,11):
    if counter==5: #คือให้หยุดทำงานที่ 5 แล้วทำงานต่อ
        continue
    print(counter)
print("จบการทำงาน")

for counter in range(1,11):
    if counter%2==0: #คือให้หาร 2 หมายถึงให้เป็นเลขคู่หยุดทำงาน แล้วแสดงแค่เลขคี่
        continue
    print(counter)
print("จบการทำงาน")