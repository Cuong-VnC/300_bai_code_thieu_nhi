'''
Bài 24: Nhập vào một số tự nhiên n (n khai báo kiểu unsigned long)
a. Số tự nhiên n có bao nhiêu chữ số.
b. Hãy tìm chữ số cuối cùng của n.
c. Hãy tìm chữ số đầu tiên của n.
d. Tính tổng các chữ số của n.
e. Hãy tìm số đảo ngược của n.
'''
# Giải ý a.
def so_chu_so(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
# Giải ý b.
def chu_so_cuoi(n):
    return n % 10
#Giải ý c.
def chu_so_dau(n):
    while n >= 10:
        n //= 10
    return n
#Giải ý d.
def tong_chu_so(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong
#Giải ý e.
def dao_nguoc(n):
    dao_nguoc = 0
    while n > 0:
        dao_nguoc = dao_nguoc * 10 + n % 10
        n //= 10
    return dao_nguoc

n = int(input("Nhập vào một số tự nhiên n: "))

print("Số chữ số của", n, "là:", so_chu_so(n))
print("Chữ số cuối cùng của", n, "là:", chu_so_cuoi(n))
print("Chữ số đầu tiên của", n, "là:", chu_so_dau(n))
print("Tổng các chữ số của", n, "là:", tong_chu_so(n))
print("Số đảo ngược của", n, "là:", dao_nguoc(n))