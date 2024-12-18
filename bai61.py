'''
Bài 61: Viết chương trình thực hiện những yêu cầu sau:
a. Tạo ngẫu nhiên mảng một chiều n phần tử nguyên có giá trị chứa trong đoạn
[-100, 100] và xuất mảng.
b. Tính tổng các số nguyên dương có trong mảng.
c. Xóa phần tử có chỉ số p (p nhập từ bàn phím) trong mảng.
'''
import random

# a. Tạo mảng ngẫu nhiên 
def generate_array(n):
    array = [random.randint(-100, 100) for _ in range(n)]
    print(f"Mảng ban đầu: {array}")
    return array

# b. Tính tổng
def ting_tong(array):
    s = 0
    for i in array:
        if i % 2 == 0:
            s += i
    return s
 
# c. Xoá phần tử chỉ số p
def xoa_phan_tu(array):
    k = int(input("Nhập chỉ số của phần tử cần xoá: "))
    del array[k]
    return array 

# Nhập số phần tử và thực hiện chương trình
try:
    n = int(input("Nhập số phần tử của mảng: "))
    

    arr = generate_array(n)
    shuffled_arr = ting_tong(arr)
    shuffle_count = xoa_phan_tu(arr)
    print(f"Mảng sau khi xoá : {shuffle_count}")
except ValueError as e:
    print(f"Lỗi: {e}")