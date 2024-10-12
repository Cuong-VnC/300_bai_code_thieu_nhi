'''
Bài 22: Viết chương trình liệt kê, đếm và tính tổng các ước số của số nguyên dương
n (n nhập từ bàn phím).
'''
n = int(input('Nhập số n: '))
tong = 0
so_uoc = 0
print(f"Các ước số của {n} là :  ",end = '')
for i in range(1,n + 1):
    if n % i == 0:
        tong += i
        so_uoc += 1
        print(i," ",end = '')
print(f"\nTổng của {so_uoc} ước số là : {tong}")