'''
49: Viết chương trình tính căn số liên tục sau:
    S = sqrt(n + sqrt(n - 1 + sqrt(n - 2 + .... +sqrt(2 + sqrt(1)))))
'''
import math

def tinh_tong(n):
    if n == 1:
        return math.sqrt(1)
    else:
        return math.pow(n + tinh_tong(n - 1), 1 / (n + 1))

n = int(input("Nhập số nguyên dương n: "))
print("Kết quả của biểu thức căn số liên tục là:", tinh_tong(n))