'''
Bài 4: Viết chương trình nhập vào 3 số thực là ba cạnh của một tam giác.Kiểm 
tra ba cạnh được nhập có hợp lệ hay không.Nếu không hợp lệ,hãy cho biết loại 
tam giác và tính diện tích tam giác đó.
'''
import math
a = float(input('nhập độ dài cạnh a: '))
b = float(input('nhập độ dài cạnh b: '))
c = float(input('nhập độ dài cạnh c: '))
if ((a + b) > c) or ((a + c) > b) or ((b + c) > a):
    if ((a**2 + b**2) == c**2) or ((a**2 + c**2) == b**2) or ((b**2 + c**2) == a**2):
        print("Đây là một tam giác vuông")
    elif (a == b == c):
        print('Đây là tam giác đều')
    elif  (a == b) or (a ==c) or (b == c):
        print('Đây là tam giác cân')
    else:
        print('Đây là tam giác thường')
    p = (a + b + c) / 2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print(f"Diện tích của tam giác có cạnh {a},{b},{c} là : {s:.2f}")
else:
    print('Đây không phải là tam giác!')
