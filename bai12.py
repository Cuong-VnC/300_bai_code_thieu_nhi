'''
Bài 12: Viết chương trình giải hệ phương trình 2 ẩn:
        a1*x + b1*y = c1
        a2*x + b2*y = c2
Các hệ số a1,a2,b1,b2,c1,c2 nhập từ bàn phím.Xét tất cả các trường hợp.       
'''
def giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2):
  # Tính định thức của ma trận hệ số
  D = a1*b2 - a2*b1
  if D != 0:
    # Hệ phương trình có nghiệm
    x = (b2*c1 - b1*c2) / D
    y = (a1*c2 - a2*c1) / D
    return x, y
  elif D == 0 and (b2*c1 - b1*c2 == 0 or a1*c2 - a2*c1 == 0):
    # Hệ phương trình vô số nghiệm
    return "Hệ phương trình có vô số nghiệm"
  else:
    # Hệ phương trình vô nghiệm
    return "Hệ phương trình vô nghiệm"

# Nhập hệ số 
a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c1 = float(input("Nhập c1: "))
c2 = float(input("Nhập c2: "))

ket_qua = giai_he_phuong_trinh(a1, b1, a2, b2, c1, c2)
print("Kết quả:", ket_qua)