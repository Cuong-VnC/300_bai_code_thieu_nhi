'''
Bài 9: Viết chương trình nhập vào số x chỉ số đo của một góc, tính bằng phút. Cho
biết nó thuộc góc vuông thứ bao nhiêu của vòng tròn lượng giác.
Tính cos(x).
'''
import math
goc_phut = float(input('Nhập số đo của góc đó: '))
if goc_phut < 0:
    print('Đây không phả góc.Lưu ý góc luôn lớn hơn 0')
else:
    #Chuyển đổi đơn vị phút sang đơn vị độ
    do = goc_phut / 60
    #Chuyển sang đơn vị radian
    goc_radi = (do * math.pi) / 180
    if (do > 0) and (do <= 90):
        print("X thuộc góc vuông thứ 1")
        tinh_cos = math.cos(goc_radi)
        print(f'cos({goc_phut}) = {tinh_cos:.4f}')
    elif (do > 90) and (do <= 180):
        print("X thuộc góc vuông thứ 2")
        tinh_cos = math.cos(goc_radi)
        print(f'cos({goc_phut}) = {tinh_cos:.4f}')
    elif (do > 180) and (do <= 270):
        print("X thuộc góc vuông thứ 3")
        tinh_cos = math.cos(goc_radi)
        print(f'cos({goc_phut}) = {tinh_cos:.4f}')
    else:
        print("X thuộc góc vuông thứ 4")
        tinh_cos = math.cos(goc_radi)
        print(f'cos({goc_phut}) = {tinh_cos:.4f}')