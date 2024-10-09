'''
Bài 10: Số bảo hiểm xã hội của Canada (SIN - Canadian Social Insurance Number)
là một số có 9 chữ số, được kiểm tra tính hợp lệ như sau:
- Số phải nhất (vị trí là 1, tính từ phải sang), là số kiểm tra (check digit).
- Trọng số được tính từ phải qua trái (không tính check digit), bằng s1 + s2:
+ s1 là tổng các số có vị trí lẻ.
+ Các số có vị trí chẵn nhân đôi. Nếu kết quả nhân đôi có hai chữ số thì kết quả là
tổng của hai chữ số này. s2 là tổng các kết quả.
SIN hợp lệ có tổng trọng số với số kiểm tra chia hết cho 10.
Ví dụ: SIN 193456787
- Số kiểm tra là 7 (màu xanh tô đậm).
- Trọng số là tổng của s1 và s2, với:
+ s1 = 1 + 3 + 5 + 7 = 16
+ Các số có vị trí chẵn nhân đôi: (9 * 2) (4 * 2) (6 * 2) (8 * 2)  18 8 12 16
s2 = (1 + 8) + 8 + (1 + 2) + (1 + 6) = 27
Trọng số bằng s1 + s2 = 16 + 27 = 43.
Vì tổng trọng số với số kiểm tra 43 + 7 = 50 chia hết cho 10 nên số SIN hợp lệ.
Viết chương trình nhập một số SIN. Kiểm tra xem số SIN đó có hợp lệ hay không.
Nhập 0 để thoát.
'''
so_SIN = str(input('Nhập số SIN cần kiểm tra( nhập 0 để thoát)! '))
if (len(so_SIN) < 0) and (len(so_SIN) > 9):
    print("Số SIN vừa nhập không đúng định dạng!")
elif int(so_SIN) == 0:
    exit()
else:
    i = 0 
    s1 = 0
    while i < 8:
        s1 += int(so_SIN[i])
        i += 2
    j = 1
    s2 = 0
    
    while j <= 8:
        s_phu = int(so_SIN[j])*2
        if s_phu >= 10:
            ep_kieu = str(s_phu)
            ep_kieu1 = int(ep_kieu[0])
            ep_kieu2 = int(ep_kieu[1])
            tong_so = ep_kieu1 + ep_kieu2
            s2 += tong_so
            
        else: 
            s2 += s_phu
        j += 2
    tong_can_tim = s1 + s2 + int(so_SIN[8])
    if tong_can_tim % 5 == 0:
        print('SIN hợp lệ!')
    else:
        print('SIN không hợp lệ!')