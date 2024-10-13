'''
Bài 28: Viết chương trình mô phỏng hàm ROUND của Microsoft Excel, dùng làm tròn
một số double với một số n cho trước.
'''
def so_round(so_can_lam_tron, he_so_lam_tron):

  factor = 10 ** he_so_lam_tron
  return round(so_can_lam_tron * factor) / factor

# Ví dụ sử dụng hàm
so_can_lam_tron = float(input("Nhập só thực càn làm tròn: "))
he_so_lam_tron = int(input("NHập hệ số càn làm tròn(số nguyên): "))
result = so_round(so_can_lam_tron, he_so_lam_tron)
print(result)  