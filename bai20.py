'''
Bài 20: Viết chương trình nhập số kW điện đã tiêu thụ. Tính tiền điện phải trả, biết
rằng khung giá tiền điện như sau:
  |-0kW------|--100kW----|--250kW-----|-350kW----|
  |-500đ/kW--|--800đ/kW--|--1000đ/kW--|-1500đ/kW-|
'''
#Tính số tiền tiêu thụ điện 
def tien_tieu_thu(kW):
    tien_dien = 0
    if (kW >= 0) and (kW <= 100):
        tien_dien += kW * 500
    elif (kW > 100) and (kW <= 250):
        tien_dien += 100*500 + (kW - 100)*800
    elif (kW > 250) and (kW <= 350):
        tien_dien += 100*500 + 150*800 + (kW - 250)*1000
    else:
        tien_dien += 100*500 + 150*800 + 100*1000 + (kW - 350)*1500
    return tien_dien 
kW = int(input("Nhập số điện tiêu thụ( nhập số nguyên): "))
tong_tien = tien_tieu_thu(kW)
print(f"Số tiền cần phải trả là : {tong_tien}đ")
