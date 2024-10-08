'''
Bài 2:Nhập vào toạ độ 2 điểm A(xA,yA) và B(xB,yB).Tính
khoảng cách AB.

'''
import math
print('Nhập toạ độ điểm A')
xA = float(input())
yA = float(input())
print('Nhập toạ độ điểm B')
xB = float(input())
yB = float(input())
khoang_cach = math.sqrt((xB -xA)**2 + (yB - yA)**2)
print(f"Khoảng cách AB là:  {khoang_cach:.2f}")