'''
Bài 32: Cho ni là một số nguyên dương, với định nghĩa tạo chuỗi:
  Chuỗi trên sẽ ngừng khi ni có trị 1. Các số được sinh ra gọi là hailstones (mưa đá),
Lothar Collatz đưa ra giả thuyết là dù n bắt đầu với giá trị nào đi nữa, chuỗi sẽ luôn
luôn dừng tại 1. Viết chương trình sinh ra chuỗi hailstones với n ban đầu nhập vào
từ bàn phím.                  
'''
def generate_hailstone_sequence(n):
  
  sequence = [n]
  while n != 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1
    sequence.append(n)
  return sequence

def main():
  while True:
    try:
      n = int(input("Nhập giá trị n nguyên dương: "))
      if n == 0:
        break
      if n <= 0:
        print("Vui lòng nhập lại .")
        continue

      sequence = generate_hailstone_sequence(n)
      print("Các số Hailstone của ", n, ":")
      print(sequence)
    except ValueError:
      print("Lỗi rồi!!!")

main()