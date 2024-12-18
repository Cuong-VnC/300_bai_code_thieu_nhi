'''
Bài 60: Viết chương trình thực hiện những yêu cầu sau:
a. Tạo ngẫu nhiên mảng một chiều n phần tử nguyên (n chẵn) có giá trị chứa
trong đoạn [-100, 100] và xuất mảng.
b. Viết hàm thực hiện việc trộn hoàn hảo (perfect shuffle) một mảng: sao cho
các phần tử của một nửa mảng sau xen kẽ với các phần tử của một nửa mảng
đầu. Xuất mảng sau khi trộn.
c. Xác định số lần trộn hoàn hảo để mảng trở về như ban đầu.
'''
import random

# a. Tạo mảng ngẫu nhiên và xuất mảng
def generate_array(n):
    if n % 2 != 0:
        raise ValueError("Số phần tử của mảng phải là số chẵn.")
    array = [random.randint(-100, 100) for _ in range(n)]
    print(f"Mảng ban đầu: {array}")
    return array

# b. Hàm trộn hoàn hảo (perfect shuffle)
def perfect_shuffle(array):
    mid = len(array) // 2
    shuffled = []
    for i in range(mid):
        shuffled.append(array[i])
        shuffled.append(array[mid + i])
    print(f"Mảng sau khi trộn: {shuffled}")
    return shuffled

# c. Tìm số lần trộn để mảng trở về trạng thái ban đầu
def count_shuffles_to_original(array):
    original = array[:]
    count = 0
    while True:
        array = perfect_shuffle(array)
        count += 1
        if array == original:
            break
    return count

# Nhập số phần tử và thực hiện chương trình
try:
    n = int(input("Nhập số phần tử của mảng (n chẵn): "))
    if n % 2 != 0:
        print("Số phần tử phải là số chẵn.")
    else:
        arr = generate_array(n)
        shuffled_arr = perfect_shuffle(arr)
        shuffle_count = count_shuffles_to_original(arr)
        print(f"Số lần trộn hoàn hảo để mảng trở về ban đầu: {shuffle_count}")
except ValueError as e:
    print(f"Lỗi: {e}")
    

