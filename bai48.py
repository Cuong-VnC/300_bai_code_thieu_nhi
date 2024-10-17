'''
Bài 48: Với số nguyên n cho trước, tìm ước số lẻ lớn nhất của n và ước số lớn nhất
của n là lũy thừa của 2.
'''
def tim_so(n):
    so_le_max = 1
    for i in range(n-1, 0, -1):
        if n % i == 0 and i % 2 == 1:
            so_le_max = i
            break

    uoc_max_luy_2 = 1
    while n % 2 == 0:
        n //= 2
        uoc_max_luy_2 *= 2

    return so_le_max, uoc_max_luy_2

n = int(input("Nhập số nguyên n: "))
uoc_le, uoc_luy_thua = tim_so(n)
print("Ước số lẻ lớn nhất của", n, "là:", uoc_le)
print("Ước số lớn nhất của", n, "là lũy thừa của 2 là:", uoc_luy_thua)