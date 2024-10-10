'''
Bài 15: Viết chương trình nhập vào ngày, tháng, năm (giả sử nhập đúng, không cần
kiểm tra hợp lệ). Tìm xem ngày đó là ngày thứ bao nhiêu trong năm.
'''
#Kiểm tra số ngày trong tháng
def so_ngay_trong_thang(thang, nam):
  if thang in [1, 3, 5, 7, 8, 10, 12]:
    return 31
  elif thang == 2:
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
      return 29
    else:
      return 28
  else:
    return 30
#Tính số ngày 
def tinh_so_ngay(ngay,thang):
    ngay_thu = int((30.42 * (thang - 1))) + int(ngay)
    if thang == 2:
        ngay_thu += 1
    return ngay_thu

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

print('Ngày thứ : ',tinh_so_ngay(ngay,thang))
        