'''
Bài 8: Viết chương trình giải phương trình bậc 2: ax2 + bx + c = 0 (a, b, c nhập từ
bàn phím). Xét tất cả các trường hợp có thể.
'''
import math
a = float(input('Nhập giá trị a: '))
b = float(input('Nhập giá trị b: '))
c = float(input('Nhập giá trị c: '))
if (a == 0) and (b == 0) and (c == 0):
    print('Phương trình có dạng:',a,'x^2 +',b,'x +',c,'= 0')
    print('Đây không phải phương trình bậc 2 nhưng nó có vô số nghiệm!!')
elif (a == 0) and (b != 0):
    print('Phương trình có dạng:',a,'x^2 +',b,'x +',c,'= 0')
    n = -b / c
    print(f'Đây không phải phương trình bậc 2 nhưng có một nghiệm là: x = {n}')
else:
    print('Phương trình có dạng:',a,'x^2 +',b,'x +',c,'= 0')
    delta = b**2 - 4*a*c
    n1 = (-b + math.sqrt(delta)) / 2*a
    n2 = (-b - math.sqrt(delta)) / 2*a
    print(f'Phương trình đã cho có hai nghiệm là: x1 = {n1:.4f} và x2 = {n2:.4f}')
    
    
