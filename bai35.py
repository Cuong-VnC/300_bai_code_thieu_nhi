'''
Bài 35: Viết chương trình kiểm tra một số nguyên dương n có là số nguyên tố hay
không. Nếu không thì phải xác định số nguyên tố gần n nhất và bé hơn n.
'''
import math

# Hàm kiểm tra số nguyên tố
def ktso(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Hàm tìm số nguyên tố nhỏ hơn n gần nhất
def sogannhat(n):
    # Bắt đầu tìm từ n-1 trở xuống
    for i in range(n-1, 1, -1):
        if ktso(i):
            return i
    return None  # Trả về None nếu không có số nguyên tố nhỏ hơn n
#Kiểm tra lại và in kết quả
def ktlai(n):
    if ktso(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
        nearest_prime = sogannhat(n)
        if nearest_prime:
            print(f"Số nguyên tố nhỏ hơn {n} gần nhất là {nearest_prime}.")
        else:
            print(f"Không tìm thấy số nguyên tố nhỏ hơn {n}.")

# Nhập số nguyên dương từ người dùng
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra và in kết quả
ktlai(n)
