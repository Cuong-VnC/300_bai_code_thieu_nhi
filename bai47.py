'''
Bài 47: Với n cho trước, tính tổng S, biết:
Nếu n chẵn: S = 2 + 4 + 6 + ... + n
Nếu n lẻ: S = 1 + 2 + 3 + ... + n
'''
def tinh_tong(n):
    s = 0 
    if n % 2 == 0:
        i = 2
        while i <= n:
            s += i
            i += 2
        print(f"Tổng S ={s}")
    else:
        for  i in range(1, n + 1):
            s += i
        print(f"Tổng S ={s}")
n = int(input("Nhập Giá Trị n = "))
tinh_tong(n)
            
        