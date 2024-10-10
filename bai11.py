'''
Bài 11: Viết trò chơi bao - đá - kéo với luật chơi: bao thắng đá, đá thắng kéo, kéo
thắng bao. Người dùng nhập vào một trong ba ký tự b (bao), d (đá), k (kéo); máy
tính sinh ngẫu nhiên một trong ba ký tự trên, thông báo kết quả chơi.
'''
#Khởi tạo thư viện random
import random
ky_tu = input('Nhập kí tự (b - d - k), ký tự khác để thoát : ')
diem_human = 0
diem_computer = 0
#Kiểm tra kí tự vừa nhập vào từ bàn phím có thoả mãn 
#đề bài không???
if ('b' in ky_tu) or ('d' in ky_tu) or ('k' in ky_tu):
    while ('b' in ky_tu) or ('d' in ky_tu) or ('k' in ky_tu):
        computer = random.randint(1,4)
        if computer == 1:
            print('Computer : b')
        elif computer == 2:
            print('Computer : d')
        else: 
            print('Computer : k')
        if ('b' in ky_tu) and (computer == 1):
            diem_human += 0
            diem_computer += 0
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer}")
        elif ('b' in ky_tu) and (computer == 2):
            diem_human += 1
            diem_computer += 0
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer}")
        elif ('b' in ky_tu) and (computer == 3):
            diem_human += 0
            diem_computer += 1
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer}")
        elif ('d' in ky_tu) and (computer == 1):
            diem_human += 0
            diem_computer += 1
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer}")
        elif ('d' in ky_tu) and (computer == 2):
            diem_human += 0
            diem_computer += 0
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer}") 
        elif ('d' in ky_tu) and (computer == 3):
            diem_human += 1
            diem_computer += 0
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer}")
        elif ('k' in ky_tu) and (computer == 1):
            diem_human += 1
            diem_computer += 0
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer}") 
        elif ('k' in ky_tu) and (computer == 2):
            diem_human += 0
            diem_computer += 1
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer + 1}") 
        else:
            diem_human += 0
            diem_computer += 0
            print(f"Tỷ số human - computer: {diem_human} - {diem_computer}")
        ky_tu = input('Nhập kí tự (b - d - k), ký tự khác để thoát : ')
else:
    exit()
                    
        
    
    