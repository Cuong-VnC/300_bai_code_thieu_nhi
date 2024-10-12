'''
Bài 23: Viết chương trình tìm các số hoàn hảo (perfect number) nhỏ hơn một số
nguyên dương n cho trước. Biết số hoàn hảo là số nguyên dương, bằng tổng các ước
số thực sự của nó (ví dụ: 28 = 14 + 7 + 4 + 2 + 1).
'''
def tim_so(n):

  so_hoan_hao = []
  for i in range(1, n):
    tong_uoc = 0
    for j in range(1, i):
      if i % j == 0:
        tong_uoc += j
    if tong_uoc == i:
      so_hoan_hao.append(i)
  return so_hoan_hao

n = int(input("Nhập số nguyên dương n: "))
ket_qua = tim_so(n)
print(f"Các số hoàn hảo nhỏ hơn {n} là: {ket_qua}")

        