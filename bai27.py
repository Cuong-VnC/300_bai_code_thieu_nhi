'''
Bài 27: Nhập vào một số nguyên dương n, phân tích n thành
các thừa số nguyên tố.
'''
import math

def phan_tich_thua_so_nguyen_to(n):
  """Hàm phân tích số nguyên dương n thành thừa số nguyên tố"""
  i = 2
  while i <= math.sqrt(n):
    while n % i == 0:
      print(i,'*', end=" ")
      n //= i
    i += 1
  if n > 1:
    print(n)

# Nhập số nguyên dương
n = int(input("Nhập số nguyên dương n: "))
print("kết quả phân tích là : ",end= '')
# Gọi hàm phân tích
phan_tich_thua_so_nguyen_to(n)