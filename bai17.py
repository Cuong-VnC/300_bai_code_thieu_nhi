'''
Bài 17: Viết chương trình tạo lịch trực cho 5 bạn: A, B, C, D, E. Nhập năm và thứ (0
- 6, 0 là Chúa Nhật, 1 là thứ Hai, ...) cho ngày đầu năm. Sau đó nhập một tháng
trong năm và in lịch trực của tháng đó. Lưu ý 5 bạn trực lần lượt theo thứ tự trên,
ngày Chúa nhật không ai trực và bạn A sẽ trực ngày đầu tiên của năm.
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

def in_lich_truc(nam, thu_dau_nam, thang):
  ten_ban = ["A", "B", "C", "D", "E"]
  so_ban = len(ten_ban)

  # Tìm số ngày của tháng
  so_ngay = 31
  if thang in [4, 6, 9, 11]:
    so_ngay = 30
  elif thang == 2:
    so_ngay = 28
    if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
      so_ngay = 29

  # In tiêu đề
  print(f"Lịch trực tháng {thang} năm {nam}")
  print(" CN  T2  T3  T4  T5  T6  T7")

  # Khởi tạo biến để theo dõi người trực
  thu = thu_dau_nam
  ban_truc = 0
  ngay = 1  
  # In lịch trực
  for ngay in range(1, so_ngay + 1):
    # In khoảng trắng cho các ngày trước ngày đầu tiên của tháng
    if ngay == 1:
      print("   " * thu, end="")

    # Nếu là Chủ Nhật thì không ai trực
    if thu != 0:
      print(f"{ten_ban[ban_truc]:2s}", end="  ")
      ban_truc = (ban_truc + 1) % so_ban
    else:
      print("  ", end="  ")

    thu = (thu + 1) % 7
    ngay += 1
    
    

    # Xuống dòng khi đến cuối tuần
    if thu == 0:
      print()

# Nhập dữ liệu
nam = int(input("Nhập năm: "))
thu_dau_nam = int(input("Nhập thứ của ngày đầu năm (0-6): "))
thang = int(input("Nhập tháng: "))

# In lịch trực
in_lich_truc(nam, thu_dau_nam, thang)