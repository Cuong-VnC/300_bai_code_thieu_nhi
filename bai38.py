'''
Bài 38: Nhập vào một số tiền n (nghìn đồng, n > 5) nguyên dương. Đổi số tiền này
ra ba loại tiền giấy 1000 VNĐ, 2000 VNĐ, 5000 VNĐ.
Tìm phương án đổi tiền sao cho loại tiền 2000VNĐ chiếm hơn phân nửa số tờ bạc phải
đổi ít nhất.
'''
def doi_tien(n):
  """
  Đổi số tiền n (nghìn đồng) thành các tờ 5000, 2000 và 1000 VNĐ.

  Args:
    n: Số tiền cần đổi (nghìn đồng).

  Returns:
    Một tuple gồm số tờ 5000, 2000 và 1000 VNĐ tương ứng.
  """

  so_to_5000 = n // 5000
  n %= 5000

  # Đảm bảo số tờ 2000 chiếm hơn một nửa
  so_to_2000 = n // 2000
  so_to_1000 = n % 2000

  # Kiểm tra và điều chỉnh để số tờ 2000 chiếm hơn một nửa
  tong_so_to = so_to_5000 + so_to_2000 + so_to_1000
  while 2 * so_to_2000 <= tong_so_to:
    so_to_2000 -= 1
    so_to_1000 += 2

  return so_to_5000, so_to_2000, so_to_1000

# Nhập số tiền cần đổi
n = int(input("Nhập số tiền cần đổi (nghìn đồng): "))

# Kiểm tra điều kiện n > 5
if n <= 5:
  print("Số tiền nhập vào không hợp lệ.")
else:
  so_to_5000, so_to_2000, so_to_1000 = doi_tien(n)
  print(f"Số tờ 5000 VNĐ: {so_to_5000}")
  print(f"Số tờ 2000 VNĐ: {so_to_2000}")
  print(f"Số tờ 1000 VNĐ: {so_to_1000}")