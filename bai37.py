'''
Bài 37: Viết chương trình nhập số nguyên dương n. Tìm số nguyên dương m lớn nhất
sao cho: 1 + 2 + ... + m < n.
'''
def tim_so_m_lon_nhat(n):
  m = 0
  while m*(m+1)//2 < n:
    m += 1
  return m - 1

n = int(input('NHập giá trị n: '))
ket_qua = tim_so_m_lon_nhat(n)
print("Số m lớn nhất là:", ket_qua)