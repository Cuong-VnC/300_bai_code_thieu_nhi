'''
Bài 14: Viết chương trình nhập vào ngày, tháng, năm (giả sử nhập đúng, không cần
kiểm tra hợp lệ). Tìm ngày, tháng, năm của ngày tiếp theo.
Tương tự, tìm ngày, tháng, năm của ngày ngay trước đó.
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
#Tính ngày tiếp theo
def ngay_tiep_theo(ngay, thang, nam):

  so_ngay = so_ngay_trong_thang(thang, nam)
  if ngay < so_ngay:
    ngay += 1
  else:
    ngay = 1
    thang += 1
    if thang > 12:
      thang = 1
      nam += 1
  return ngay, thang, nam
#Tính ngày trước đó
def ngay_truoc_do(ngay, thang, nam):
    if ngay > 1:
        ngay -= 1
    else:
        thang -= 1
        if thang < 1:
            thang = 12
            nam -= 1
        ngay = so_ngay_trong_thang(thang, nam)
    return ngay, thang, nam

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

#Gán giá trị ngày tiếp theo và ngày trước đó
ngay_sau, thang_sau, nam_sau = ngay_tiep_theo(ngay, thang, nam)
ngay_truoc, thang_truoc, nam_truoc = ngay_truoc_do(ngay, thang, nam)

print(f"Ngày tiếp theo: {ngay_sau}/{thang_sau}/{nam_sau}")
print(f"Ngày trước đó: {ngay_truoc}/{thang_truoc}/{nam_truoc}")