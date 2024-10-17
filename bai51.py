def phan_so_lien_tuc(x):
    
    if x == 0:
        raise ValueError("x cannot be zero.")
    mau_so = x + 256 / x
    for i in range(127, 1, -1):
        mau_so = x + i / mau_so
    return x + 1 / mau_so

x = float(input("Nhập giá trị x = "))
print("Kết quả = ",phan_so_lien_tuc(x))
        

            