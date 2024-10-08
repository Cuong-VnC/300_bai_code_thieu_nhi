''' 
Bài 1: 
Nhập vào diện tích S của một mặt cầu.Tính 
thể tích của hình cầu này.
'''
import math
def tinh_the_tich(S):
    if S <= 0:
        return 'Đây không phải hình cầu'
    pi = math.pi
    R = math.sqrt(S / (4*pi))
    V = (4/3) * pi * R**3
    return V
S = float(input('Nhập diện tích mặt cầu : '))
V = tinh_the_tich(S)
print(f"Thể tích của hình cầu là {V:.2f}")
                             