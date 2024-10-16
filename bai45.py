'''
Bài 45: Dùng vòng lặp lồng, với n (n < 5) nhập từ bàn phím, viết chương trình in
hai tam giác đối đỉnh bằng số, tăng theo cột từ 1 đến 2n - 1.
'''
def tam_giac_doi_dinh(n):
  for i in range(1, 2 * n):
    for j in range(1, 2 * n):
      if (j <= i and j <= 2 * n - i) or (j >= i and j >= 2 * n - i):
        print(f"{j:2d}", end="")
      else:
        print("  ", end="")
    print()

n = int(input("Enter n (n < 5): "))
if n >= 5:
    print("Nhập quá giá trị đề bài.Vui lòng nhập gt n trong khoảng n < 5:")
else:
    #in ra màn hình
    tam_giac_doi_dinh(n)   