'''
Bài 56: Viết chương trình nhập vào một số nguyên n có dấu, in ra dạng hiển thị nhị
phân và thập lục phân của n.
'''
def chuyen_doi_he_so(n,he_co_so):
    kq = ""
    while n != 0:
        du = n % he_co_so
        if du >= 10:
          du = chr(du + 55) 
        kq = str(du) + kq
        n //= he_co_so
    return kq

n = int(input("Nhập vào một số nguyên n: "))

bin_n = chuyen_doi_he_so(n, 2)
hex_n = chuyen_doi_he_so(n, 16)
print(f"Số {n} trong hệ nhị phân là: {bin_n}")
print(f"Số {n} trong hệ thập lục phân là: {hex_n}")