'''
Bài 21: Trong kỳ thi tuyển, một thí sinh sẽ trúng truyển nếu có điểm tổng kết lớn
hơn hoặc bằng điểm chuẩn và không có môn nào điểm 0.
- Điểm tổng kết là tổng điểm của 3 môn thi và điểm ưu tiên.
- Điểm ưu tiên bao gồm điểm ưu tiên theo khu vực và điểm ưu tiên theo đối tượng.
Viết chương trình nhập: điểm chuẩn của hội đồng, điểm 3 môn thi của thí sinh, khu
vực (nhập X nếu không thuộc khu vực ưu tiên) và đối tượng dự thi (nhập 0 nếu không
thuộc đối tượng ưu tiên). Cho biết thí sinh đó đậu hay rớt và tổng số điểm đạt được.
'''
def kiem_tra(diem_chuan,mon1,mon2,mon3,khu_vuc,doi_tuong):
    if ("A" in khu_vuc) and doi_tuong == 1:
        diem_thi_tong = mon1 + mon2 + mon3 + 2 + 2.5
    elif ("A" in khu_vuc) and doi_tuong == 2:
        diem_thi_tong = mon1 + mon2 + mon3 + 2 + 1.5
    elif ("A" in khu_vuc) and doi_tuong == 3:
        diem_thi_tong = mon1 + mon2 + mon3 + 2 + 1
    elif ("A" in khu_vuc) and doi_tuong == 0:
        diem_thi_tong = mon1 + mon2 + mon3 + 2 + 0
    elif ("B" in khu_vuc) and doi_tuong == 1:
        diem_thi_tong = mon1 + mon2 + mon3 + 1 + 2.5
    elif ("B" in khu_vuc) and doi_tuong == 2:
        diem_thi_tong = mon1 + mon2 + mon3 + 1 + 1.5
    elif ("B" in khu_vuc) and doi_tuong == 3:
        diem_thi_tong = mon1 + mon2 + mon3 + 1 + 1
    elif ("B" in khu_vuc) and doi_tuong == 0:
        diem_thi_tong = mon1 + mon2 + mon3 + 1 + 0
    elif ("C" in khu_vuc) and doi_tuong == 1:
        diem_thi_tong = mon1 + mon2 + mon3 + 0.5 + 2.5
    elif ("C" in khu_vuc) and doi_tuong == 2:
        diem_thi_tong = mon1 + mon2 + mon3 + 0.5 + 1.5
    elif ("C" in khu_vuc) and doi_tuong == 3:
        diem_thi_tong = mon1 + mon2 + mon3 + 0.5 + 1
    elif ("C" in khu_vuc) and doi_tuong == 0:
        diem_thi_tong = mon1 + mon2 + mon3 + 0.5 + 0
    elif ("X" in khu_vuc) and doi_tuong == 1:
        diem_thi_tong = mon1 + mon2 + mon3 + 0 + 2.5
    elif ("X" in khu_vuc) and doi_tuong == 2:
        diem_thi_tong = mon1 + mon2 + mon3 + 0 + 1.5
    elif ("X" in khu_vuc) and doi_tuong == 3:
        diem_thi_tong = mon1 + mon2 + mon3 + 0 + 1
    else:
        diem_thi_tong = mon1 + mon2 + mon3
    if diem_thi_tong  < diem_chuan:
        tb = 'Rớt'
    else:
        tb = 'Đỗ'
    return tb
diem_chuan = float(input("Nhập điểm chuẩn : "))
mon1 = float(input('Nhập điểm môn 1: '))
mon2 = float(input('Nhập điểm môn 2: '))
mon3 = float(input('Nhập điểm môn 3: '))
khu_vuc = input('Nhập khu vực(A,B,C,X): ')
doi_tuong = int(input('Nhập đối tượng(1,2,3,0): '))
thongbao = kiem_tra(diem_chuan,mon1,mon2,mon3,khu_vuc,doi_tuong)
print(f"Kết quả: {thongbao}")
