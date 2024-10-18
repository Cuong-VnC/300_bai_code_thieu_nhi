'''
Bài 57: Bit parity là bit thêm (redundant) vào dữ liệu được truyền đi, dùng để phát
hiện lỗi bit đơn trong quá trình truyền dữ liệu. Bit parity chẵn (even parity) là bit có
trị được chọn sao cho tổng số bit 1 trong dữ liệu truyền kể cả bit parity là một số
chẵn. Viết chương trình nhập vào một số nguyên n. Xác định bit parity chẵn của n.
'''
def tinh_bit_parity_chan(n):
  dem = 0
  while n > 0:
    dem += n & 1
    n >>= 1
  return dem % 2

# Nhập số nguyên n
n = int(input("Nhập vào một số nguyên n: "))

# Tính và in ra bit parity chẵn
bit_parity = tinh_bit_parity_chan(n)
print(f"Bit parity chẵn của {n} là: {bit_parity}")