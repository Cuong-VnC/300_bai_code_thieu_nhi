'''
Bài 53: Viết chương trình tính sin(x) với độ chính xác 10-4
theo chuỗi Taylor9(Taylorseries):
    sin(x)=x - x^3 / 3! + x^5/5! -....+(-1)*n*x^(2n - 1)/(2n +1)!
'''
import math
def ct_taylor(x, eps=1e-4):
    fact = 1
    s = expr = expo = x
    sign = -1
    for i in range(3, 1000, 2):
        expo *= x * x
        fact *= i * (i - 1)
        expr = expo / fact
        s += sign * expr
        sign = -sign
        if abs(expr) < eps:
            break
    return s
x = float(input("Nhập giá trị x = "))
ket_qua = ct_taylor(x)
print("sin(%.2f) = %.4f" % (x, ket_qua))
print("sin(x) trong hàm math.sin() : sin(%.2f) = %.4f" % (x, math.sin(x)))