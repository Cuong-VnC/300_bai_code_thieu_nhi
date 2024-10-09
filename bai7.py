'''
Bài 7: Viết chương trình giải phương trình bậc 1: ax + b = 0 (a, b nhập từ bàn phím).
Xét tất cả các trường hợp có thể.
'''
a = int(input('Nhập giá trị a: '))
b = int(input('Nhập giá trị b: '))
print("Phương trình của bạn là : ",a,'x +',b,'= 0')
if (a == 0) and (b == 0):
    print('Phương trình có vô số nghiệm')
elif (a == 0) and (b != 0):
    print('Phương trình đã cho vô nghiệm')
else:
    n = -b / a
    print(f"Nghiệm của phương trình đã cho là: x= {n}")
    
    
    