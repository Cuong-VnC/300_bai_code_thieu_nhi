'''
Bài 28: Viết chương trình mô phỏng hàm ROUND của Microsoft Excel, dùng làm tròn
một số double với một số n cho trước.
'''
def round_number(number, num_digits):

  factor = 10 ** num_digits
  return round(number * factor) / factor

# Ví dụ sử dụng hàm
number = float(input("Nhập só thực càn làm tròn: "))
num_digits = int(input("NHập hệ số càn làm tròn(số nguyên): "))
result = round_number(number, num_digits)
print(result)  