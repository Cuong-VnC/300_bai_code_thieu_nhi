'''
Bài 26: Nhập vào tử số, mẫu số (đều khác 0) của một phân số. Hãy rút gọn phân số
này. Chọn dạng xuất thích hợp trong trường hợp mẫu số bằng 1 và phân số có dấu.
'''
def rut_gon_phan_so(tu_so, mau_so):
 # Kiểm tra điều kiện mẫu số khác 0
  if mau_so == 0:
    print("Mẫu số không thể bằng 0.")
    return
 # Tìm ước chung lớn nhất của tử số và mẫu số
  uscln = ucln(tu_so, mau_so)
 # Rút gọn phân số
  tu_so //= uscln
  mau_so //= uscln
 # Xuất kết quả
  if mau_so == 1:
    print(tu_so)  # Nếu mẫu số bằng 1, chỉ in tử số
  else:
    # Xử lý dấu
    if tu_so * mau_so < 0:
      dau = "-"
      tu_so = abs(tu_so)
      mau_so = abs(mau_so)
    else:
      dau = ""
    print(f"{dau}{tu_so}/{mau_so}")
# Hàm tìm ước chung lớn nhất
def ucln(tu_so, mau_so):
  while mau_so != 0:
    tu_so, mau_so = mau_so, tu_so % mau_so
  return tu_so

tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

rut_gon_phan_so(tu_so, mau_so)