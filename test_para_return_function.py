# 1 โจทย์หาค่าเฉลี่ยนักเรียน
def calculate_average(*scores):
    if len(scores)==0:
        return 0
    total =sum(scores)

    average=sum(scores) / len(scores)
    return average

student_score=[20,50,60,30]
average_score = calculate_average(*student_score)
print("ค่าเฉลี่ยคือ:", average_score)

# #โจทย์ 2 แปลงอุณภูมิ จาก องศาเซลเซียส เป็น ฟาเรนไฮต์

def calsius_to_fahrenheit(celsius):
    fahrenheit=(celsius *9/5)+32
    return fahrenheit 

temp_c = 26
temp_f = calsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

# #โจทย์ 3 คำนวณส่วนลดสินค้า
def calculate_discount(price,discount_percent):
    discount_amount =(price * discount_percent / 100)
    final_price = price - discount_amount
    return final_price 

original_price = 1000
discount = 25
price_after_discount = calculate_discount(original_price,discount)
print("ราคาหลังหักส่วนลด :",price_after_discount, "บาท")

#คำนวณอายุจากปีเกิด
def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    return age

birth_year = 2000
current_year = 2025
user_age = calculate_age(birth_year, current_year)
print("อายุของคุณคือ:", user_age, "ปี")

#

