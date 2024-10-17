def tinh_tong(n):
    tong = 0
    for i in range(1,n + 1):
        tong += 1 / ((n ** 2) + i)
    return tong
n = int(input("Nhập Giá trị n = "))
print("Tổng cần tìm là: ",tinh_tong(n))