'''
Bài 33: Số tự nhiên có n chữ số là một số Armstrong (còn gọi là 
narcissistic numbers hoặc pluperfect digital invariants - PPDI)
nếu tổng các lũy thừa bậc n của các chữ số của nó bằng chính nó.
Hãy tìm tất cả các số Armstrong có 3, 4 chữ số.
Ví dụ: 153 là số Armstrong có 3 chữ số vì: 1^3 + 5^3 + 3^3 = 153
'''
def kt_armstrong(num):
  # Tính số lượng chữ số
  num_digits = len(str(num))

  # Tính tổng các lũy thừa bậc n
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

  return num == sum

def tim_armstrong(start, end):
  for num in range(start, end + 1):
    if kt_armstrong(num):
      print(num)

# Tìm các số Armstrong có 3 chữ số
tim_armstrong(100, 999)

# Tìm các số Armstrong có 4 chữ số
tim_armstrong(1000, 9999)
    
