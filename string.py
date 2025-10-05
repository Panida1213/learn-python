#ทำให้เป็นพิมพ์เล็กหรือพิมพ์ใหญ่
name="PanidaPholdongnok"
print(name.upper())
name="PanidaPholdongnok"
print(name.lower())
#ตรวจสอบเพศจากชื่อ
name=input("ป้อนชื่อของคุณ:")
if name.startswith("Mr"):
    print("Men")
elif name.startswith("Ms"):
    print("Women")

#ตรวจสอบคำลงท้าย
month=input("ป้อนเดือน: ")
if month.endswith("คม"):
    print("เดือนนี้มี 31 วัน")
elif month.endswith("ยน"):
    print("เดือนนี้มี 30 วัน")

#ค้นหาคำ
text="Hello"
print(text.find("Hello"))

#ค้นหาจำนวนตัวหนังสือ
text="Sawaddee"
print(text.count("e"))

#แทนที่ หรือ update ข้อความ
text="ปีนี้ทั้งปีเป็นปี 2567"
update = text.replace("2567","2568")
print(update)

#การลบช่องว่างระหว่สงข้อความ ซ้ายขวา
text=" Python ".strip()
print(len(text))

#การจัดรูปแบบ String โดย Format
text="my name {0} age {1} in {2} year".format("Panida",23,2025)
print(text)