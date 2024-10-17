'''
Bài 46: Viết chương trình kiểm tra hai vế của công thức sau, với n cho trước:
        Tổng i^3(từ i = 1 đến n) = (n^2 * (n + 1)) / 4
'''
def kiem_tra(n):
    #Kiểm tra vế trái
    s_trai = 0
    for i in range(1,n + 1):
        s_trai += i**3
    print(f"Vế trái = {s_trai}")
    s_phai = ((n**2) * ((n + 1)**2)) / 4
    print(f"Vế phải = {s_phai}")
n = int(input("Nhập giá trị n = "))
kiem_tra(n)