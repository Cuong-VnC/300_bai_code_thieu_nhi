'''
Bài 54: Dùng vòng lặp, tính tổ hợp chập k của n (k < n < 25):
            nCk = n! / k! * (n - k)!
    Kiểm chứng công thức: nCk = nC(n - k)
'''
def to_hop(n, k):
    if k < 0 or k > n:
        raise ValueError("Giá trị nHập không hợp lệ.")
    tu_so = 1
    mau_so = 1
    for i in range(1, k + 1):
        tu_so *= n
        mau_so *= i
        n -= 1
    return tu_so // mau_so

def kt_cong_thuc(n, k):
    c1 = to_hop(n, k)
    c2 = to_hop(n, n - k)
    return c1 == c2

k = int(input("Nhập giá trị k(k < n < 25): "))
n = int(input("Nhập giá trị n(k < n < 25): "))
ket_qua1 = to_hop(n, k)
print("C(", n, ", ", k, ") = ", ket_qua1)
ket_qua2 = kt_cong_thuc(n, k)
print("Formula verification:", ket_qua2)