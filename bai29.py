'''
Bài 29: Lập bảng so sánh hai thang đo nhiệt độ Fahrenheit và Celsius4
trong các đoạn sau:
- Đoạn [0oC, 10oC], bước tăng 1
oC.
'''
def doi_sang_f(do_C):
  """Chuyển đổi từ độ C sang độ F"""
  return (do_C * 9/5) + 32

def tao_bang(start_celsius, end_celsius, start_fahrenheit, end_fahrenheit, step):
  """Tạo bảng so sánh nhiệt độ"""

  print("Bảng so sánh nhiệt độ Celsius và Fahrenheit")
  print(" |---------------------------|")
  print(f" | {'Độ C':^10}|  {'Độ F':^10}   |")
  print(" |---------------------------|")

  for celsius in range(start_celsius, end_celsius+1, step):
    fahrenheit = doi_sang_f(celsius)
    print(f" | {celsius:^10}|   {fahrenheit:^10.2f}  |")

# Gọi hàm để tạo bảng so sánh
tao_bang(0, 10, 32, 42, 1)
