#สร้าง Functions แบบมีพารามิเตอร์

def Hello(time,username,age): #parameter
    print("สวัสดี",time,username)
    print("ปีนี้คุณมีอายุ",age,"ปี")

def saveEmployee(name,department,salary):
    print(f"ชื่อ{name},แผนก{department},")
    print(f"เงินเดือน{salary} บาท")
    print("-----------")

def showTable(num):
    print(f"-----สูตรคุณแม่{num}-------")
    for i in range(1,13):
        print(f"{num} x {i}={num*i}")
#เรียกใช้งาน
myTime="ตอนเช้า"
Hello(myTime,"Panida",23) #arguments
showTable(8)

saveEmployee("พนิดา","คอนเทนต์",30000)
saveEmployee("รัศมี","การตลาด",35000)