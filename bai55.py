'''
Bài 55: Tính căn bậc hai của một số nguyên dương x bằng thuật toán Babylonian.
Kiểm tra kết quả với hàm chuẩn sqrt().
'''
import math
def babylonian_sqrt(x, epsilon=1e-6):
    if x <= 0:
        raise ValueError("Số cần tính phải là số không âm và khác 0")
    y = x / 2 
    while abs(y * y - x) > epsilon:
        y = (y + x / y) / 2
    return y

x = int(input("Nhập giá trị x = "))
ket_qua = babylonian_sqrt(x)
print("Căn bậc hai của", x, "tính bằng thuật toán Babylon:", ket_qua)
print("Căn bậc hai của", x, "tính bằng hàm sqrt():", math.sqrt(x))