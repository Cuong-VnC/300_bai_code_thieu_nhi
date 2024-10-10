'''
Bài 13: Viết chương trình nhập vào ngày, tháng, năm. Kiểm tra ngày và tháng nhập
có hợp lệ hay không. Tính thứ trong tuần của ngày đó.
'''
def so_ngay_trong_thang(thang, nam):
  #Kiểm tra số ngày trong tháng vừa nhập
  if thang in [1, 3, 5, 7, 8, 10, 12]:
    return 31
  elif thang == 2:
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
      return 29
    else:
      return 28
  else:
    return 30

def tinh_thu(ngay, thang, nam):
  # Sử dụng CT Zellers để tính thứ trong tuần  
  t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  if thang < 3:
      nam -= 1
      thang += 12
  a, y, m, d = nam // 100, nam % 100, thang, ngay
  w = (d + t[m-1] + y + y//4 + a//4 - 2*a) % 7
  return w

def kiem_tra_ngay(ngay, thang, nam):
  #Kiểm tra tính hợp lệ của ngày, tháng, năm.
  if nam < 0 or thang < 1 or thang > 12 or ngay < 1 or ngay > so_ngay_trong_thang(thang, nam):
    return False
  else:
    return True

# Nhập dữ liệu
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Kiểm tra tính hợp lệ và in kết quả ra màn hình
if kiem_tra_ngay(ngay, thang, nam):
    thu = tinh_thu(ngay, thang, nam)
    if (thu == 0):
        print(f"Ngày {ngay}/{thang}/{nam} là Chúa nhật trong tuần.")
    elif (thu == 1):
        print(f"Ngày {ngay}/{thang}/{nam} là Thứ hai trong tuần.")
    elif (thu == 2):
        print(f"Ngày {ngay}/{thang}/{nam} là Thứ ba trong tuần.")
    elif (thu == 3):
        print(f"Ngày {ngay}/{thang}/{nam} là Thứ tư trong tuần.")
    elif (thu == 4):
        print(f"Ngày {ngay}/{thang}/{nam} là Thứ năm trong tuần.")
    elif (thu == 1):
        print(f"Ngày {ngay}/{thang}/{nam} là Thứ sáu trong tuần.")
    else:
        print(f"Ngày {ngay}/{thang}/{nam} là Thứ bảy trong tuần.")      
        
else:
  print("Ngày,tháng,năm nhập không hợp lệ.")
  