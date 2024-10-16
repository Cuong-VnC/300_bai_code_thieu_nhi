'''
Bài 41: Viết chương trình tìm cách thay thế các dấu hỏi (?) bởi các dấu 4 phép tính
số học +, -, *, /, trong biểu thức dưới đây sao cho biểu thức có giá trị bằng 36.
                 ((((1 ? 2) ? 3) ? 4) ? 5) ? 6
'''
import itertools

def tim_ct(ct_chung):
    phep_tinh = ['+', '-', '*', '/']
    all_combinations = itertools.product(phep_tinh, repeat=5)

    for combination in all_combinations:
        ket_qua = ct_chung
        for i, op in enumerate(combination):
            ket_qua = ket_qua.replace('?', op, 1)  # Thay thế dấu hỏi thứ i bằng phép tính
        try:
            s = eval(ket_qua)
            if s == 36:
                print(ket_qua)
        except ZeroDivisionError:
            pass  # Bỏ qua trường hợp chia cho 0

ct_chung = "((((1 ? 2) ? 3) ? 4) ? 5) ? 6"
tim_ct(ct_chung)