#para+return function ฟังก์ชันแบบมีการรับค่าและส่งค่าออกไปทำงานนอกฟังก์ชัน
def chackNumber(number):
    if number%2==0:
        return "เลขคู่"
    else:
        return "เลขคี่"

def summation(*data):
    total=0
    for item in data:
        total+=item
    return total
print(summation(23,46))
print(summation(59,90,13)) 

#result = chackNumber(70)
#print("ผลลัพธ์ = ",result)   