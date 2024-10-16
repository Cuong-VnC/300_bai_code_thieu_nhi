'''
Bài 44: Dùng vòng lặp lồng, viết chương trình in ra tam giác cân đặc và rỗng, tạo từ
các dấu sao (*), có độ cao là n nhập từ bàn phím.
'''
def draw_triangle(n, hollow=False):
  for i in range(n):
    # In khoảng trắng ở đầu mỗi hàng (cho tam giác rỗng)
    for j in range(n - i - 1):
      print(" ", end="")
    # In dấu sao
    for j in range(2 * i + 1):
      if hollow and i != 0 and j != 0 and j != 2 * i:
        print(" ", end="")
      else:
        print("*", end="")
    print()

# Nhập độ cao của tam giác
n = int(input("Nhập độ cao của tam giác: "))

# Vẽ tam giác đặc
print("Tam giác đặc:")
draw_triangle(n)

# Vẽ tam giác rỗng
print("Tam giác rỗng:")
draw_triangle(n, True)
    