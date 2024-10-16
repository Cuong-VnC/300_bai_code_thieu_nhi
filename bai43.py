'''
Bài 43: Tìm số Fibonacci thứ n (0 < n < 40), dùng vòng lặp (không dùng đệ quy).
'''
def tim_so(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        so_truoc1 = 1
        so_truoc2 = 1
        so_n = 1
        for _ in range(2,n):
            so_n = so_truoc1 + so_truoc2
            so_truoc1 = so_truoc2
            so_truoc2 = so_n
    return so_n
n = int(input("nhập vị trí càn tìm: "))
if n < 40:
    ket_qua = tim_so(n)
    print(f"số fibonacci thứ{n} là: {ket_qua}")
else:
    print("số không đúng.Vui lòng nhập lại với n < 40")
        