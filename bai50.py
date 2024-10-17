'''
Bài 50:Phân số liên tục (continued fraction) ký hiệu [b1, b2, ..., bk], có dạng:
                s / t = 1 /(b1+ (1 / (b2 + 1 / ....(b(k - 1) + 1 / bk))))

b1, b2, ..., bk là các số tự nhiên. Cho s và t, viết chương trình tìm [b1, b2, ..., bk].
'''
def so_lien_tuc(s, t):
    if s == 0:
        return []

    he_so = []
    while t != 1:
        b = s // t
        he_so.append(b)
        s, t = t, s % t

    he_so.append(s)
    return he_so

s = int(input("nhập giá trị s (0 < s < t): "))
t = int(input("nhập giá trị t (0 < s < t): "))
result = so_lien_tuc(s, t)
print(result)