'''
Bài 36:Viết chương trình in ra n số nguyên tố đầu tiên(n nhập từ bàn phím).
'''
import math

# Hàm kiểm tra số nguyên tố
def ktsonguyento(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if n % i == 0:
            return False
    return True

# Hàm in ra n số nguyên tố đầu tiên
def inramanhinh(n):
    count = 0   # Biến đếm số lượng số nguyên tố đã tìm thấy
    num = 2     # Bắt đầu kiểm tra từ số 2
    prime_list = []  # Danh sách lưu trữ các số nguyên tố

    while count < n:
        if ktsonguyento(num):
            prime_list.append(num)
            count += 1
        num += 1
    
    # In ra danh sách các số nguyên tố
    print(f"{n} số nguyên tố đầu tiên là:")
    print(prime_list)

# Nhập số n từ bàn phím
n = int(input("Nhập số lượng số nguyên tố cần in: "))

# In ra n số nguyên tố đầu tiên
inramanhinh(n)
