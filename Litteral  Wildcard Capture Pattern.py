#ทำงานคล้ายๆ if elif else แต่ทำงานร่วมกับ list tuple dictionary
#1 Literal Pattern
service=300
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("สอบถามยอดเงิน")
    case None:
        print("ข้อมูลไม่ถูกต้อง")
#2 Wildcard pattern ใช้สำหรับในกำหนดเงื่อนไขที่ไม่ตรงกับเงื่อนไขใดๆที่ได้กำหนดขึ้นมา
    #case _: #default case
        #print("หมายเลขบริการไม่ถูกต้อง")
#3 Capture Pattern นำข้อมูลในตัวแปรมาอ้างอิงการทำงานในพื้นที่ Match case ที่เป็น case นอกเหนือจาก case ที่มี
    case service:
        print(f"ไม่พบหมายเลขบริการ {service} ในระบบ กรุณาทำรายการใหม่")