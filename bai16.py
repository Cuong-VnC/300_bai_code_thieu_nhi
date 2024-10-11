''''
Bài 16: Viết chương trình nhập vào một năm (> 1582), in lịch của năm đó. Tính thứ
cho ngày đầu năm bằng công thức Zeller (bài 14, trang 6).
'''
#Tính thứ củA một ngày theo CT zeller
def tinh_thu(ngay, thang, nam):
  if thang < 3:
    thang += 12
    nam -= 1

  j = nam // 100
  k = nam % 100
  h = ngay
  m = thang
  q = (h + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
  return q

def in_lich(nam):
    
  ten_thang = ["Tháng Một", "Tháng Hai", "Tháng Ba", "Tháng Tư", "Tháng Năm", "Tháng Sáu","Tháng Bảy", "Tháng Tám", "Tháng Chín", "Tháng Mười", "Tháng Mười Một", "Tháng Mười Hai"]

  ten_ngay = ["CN", "T2", "T3", "T4", "T5", "T6", "T7"]

  # Tính thứ của ngày đầu năm
  thu = tinh_thu(1, 1, nam)

  # In tiêu đề
  print(f"Lịch năm {nam}")

  # Kiẻm tra qua từng tháng
  for thang in range(1, 13):
    # In tên tháng
    print(f"\n{ten_thang[thang - 1]}")

    # In ngày
    print(" CN  T2  T3  T4  T5  T6  T7")

    # Tìm số ngày
    so_ngay = 31
    if thang in [4, 6, 9, 11]:
      so_ngay = 30
    elif thang == 2:
      so_ngay = 28
      if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
        so_ngay = 29

    # In các ngày
    ngay = 1
    while ngay <= so_ngay:
      # In khoảng trắng cho các ngày 
      # trước ngày đầu tiên của tháng
      if ngay == 1:
        print("   " * thu, end="")

      print(f"{ngay:2d}", end="  ")
      thu = (thu + 1) % 7
      ngay += 1

      # Xuống dòng khi đến cuối tuần
      if thu == 0:
        print()

nam = int(input("Nhập năm (> 1582): "))

in_lich(nam)