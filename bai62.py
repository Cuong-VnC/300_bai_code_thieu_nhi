'''
Bài 62: Viết chương trình thực hiện những yêu cầu sau:
a. Tạo ngẫu nhiên mảng một chiều n phần tử nguyên dương có giá trị chứa
trong đoạn [10, 20] và xuất mảng.
b. Kiểm tra tổng các số chẵn ở vị trí lẻ có bằng tổng các số lẻ ở vị trí chẵn không.
c. Xác định xem mảng có cặp số nguyên tố cùng nhau (coprime) nào không.

Note: Hai số nguyên dương a và b được gọi là hai số nguyên tố cùng nhau nếu
ước số chung lớn nhất của hai số a và b là 1.
'''

import random
from math import gcd

# a. Tạo mảng ngẫu nhiên 
def taomang(n):
    array = [random.randint(10, 20) for _ in range(n)]
    print(f"Mảng ban đầu: {array}")
    return array

# b. Kiểm tra tổng chẵn lẻ của mảng
def kiemtrachanle(array):
    s_chan = 0
    for i in range(1,len(array),2):
       if array[i] % 2 == 0:
           s_chan += array[i]

    s_le = 0
    for i in range(0,len(array),2):
        if array[i] % 2 !=0:
            s_le += array[i]
    return s_chan == s_le

# c. Xác định cặp nguyên tố cùng nhau
def nguyencug(array):
    capso = []
    for i in range(len(array)):
        for j in range(i + 1,len(array)):
            if gcd(array[i], array[j]) == 1:  
                capso.append((array[i], array[j]))
    return capso

try: 
    n = int(input("Nhập số phần tử củ mảng: "))
    if n <= 0:
        print("Vui lòng nhập số phần tử lớn hơn 0: ")
    else:
        arr = taomang(n)
        if kiemtrachanle(arr):
            print("Tổng chẵn ở vị trí lẻ bằng tổng lẻ ở vị tró chẵn")
        else:
            print("Tổng chẵn ở vị trí lẻ không bằng tổng lẻ ở vị tró chẵn")
        capso = nguyencug(arr)
        if capso:
            print(f"Các cặp số nguyên tố cùng nhau: {capso}")
        else:
            print("Không có cặp số nguyên tố cùng nhau nào trong mảng!")
except ValueError as e:
    print(f"Lỗi: {e}")
    
    