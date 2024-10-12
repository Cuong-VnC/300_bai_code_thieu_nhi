import datetime

def tinh_khoang_cach_thoi_gian(gio_bat_dau, phut_bat_dau, giay_bat_dau, gio_ket_thuc, phut_ket_thuc, giay_ket_thuc):
  thoi_diem_bat_dau = datetime.datetime(2023, 1, 1, gio_bat_dau, phut_bat_dau, giay_bat_dau)
  thoi_diem_ket_thuc = datetime.datetime(2023, 1, 1, gio_ket_thuc, phut_ket_thuc, giay_ket_thuc)

  # Tính hiệu
  khoang_cach = thoi_diem_ket_thuc - thoi_diem_bat_dau

  # Trích xuất giờ, phút, giây từ hiệu
  gio, phut, giay = khoang_cach.seconds // 3600, khoang_cach.seconds % 3600 // 60, khoang_cach.seconds % 60

  return gio, phut, giay

# Nhập liệu từ người dùng
gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
phut_bat_dau = int(input("Nhập phút bắt đầu: "))
giay_bat_dau = int(input("Nhập giây bắt đầu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))
phut_ket_thuc = int(input("Nhập phút kết thúc: "))
giay_ket_thuc = int(input("Nhập giây kết thúc: "))

# Gọi hàm tính khoảng cách và in kết quả
gio, phut, giay = tinh_khoang_cach_thoi_gian(gio_bat_dau, phut_bat_dau, giay_bat_dau, gio_ket_thuc, phut_ket_thuc, giay_ket_thuc)
print(f"Khoảng thời gian là: {gio} giờ {phut} phút {giay} giây")