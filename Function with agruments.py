# Agruments เป็นตัวแปรที่ถูกส่งมาให้ฟังก์ชัน กรณีที่มีการส่งมาหลายๆค่าจะแบ่งการทำงานเป็น 2 รูปแบบ คือ Args (แบบลำดับ)
#และ Kwargas แบบกำหนดชื่อ 

#แบบทดสอบ Args
def saveinfo(*args):
    print(f"ชื่อ {args[0]},{args[1]}")
    print(f"อายุ {args[2]}")
    print(f"เงินเดือน {args[3]}")

saveinfo("Jane","Smit",23,25000)

#แบบทดสอบ Kwargas
def saveinfo(**kwargs):
    print(f"ชื่อ {kwargs["name"]},{kwargs["lastname"]}")
    print(f"อายุ {kwargs["age"]}")
    print(f"เงินเดือน {kwargs["salary"]}")

saveinfo(name="Jane",lastname="Smit",age=23,salary=25000)

#แบบทำสอบ 2 
def show_product_info(**kwargs):
    print(f"name:{kwargs["namephone"]}")
    print(f"pricce:{kwargs["price"]}")
    print(f"category:{kwargs["category"]}")

show_product_info(namephone="iphone",price=40000,category="smartphone")

#แบบทำสอบ 3 รวม args กับ kwargs
def describe_students(*args,**kwargs):
    print(f"Students:{args[0]},{args[1]},{args[2]}")
    print(f"Room:{kwargs['room']}")
    print(f"Teacher:{kwargs['teacher']}")

describe_students("Jane","John","Bow",room="A3",teacher="Taylor")