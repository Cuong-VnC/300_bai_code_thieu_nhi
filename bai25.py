'''
Bài 25: Nhập vào hai số nguyên dương a, b. Tính ước số chung lớn nhất và bội số
chung nhỏ nhất của a, b.
'''
def uscln(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def bscnn(a, b):
    gt = a * b // uscln(a, b)
    return gt

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b))