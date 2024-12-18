'''
Bài 59: Nhập vào năm Dương lịch, xuất tên năm Âm lịch. Xuất năm Dương lịch kế
tiếp có cùng tên năm Âm lịch. Biết bánh xe tính hai chu kỳ Can - Chi như sau:
        Năm có cùng tên Âm lịch với năm y là y ± k * 60 (60 là BSCNN của hai chu
        kỳ 10 và 12). Mốc tính Can Chi, lấy năm 0 là năm Canh Thân.
'''

def lichCanChi(nam):
    can = ["Canh", "Tan", "Nham", "Quy", "Giap", "At", "Binh", "Dinh", "Mau", "Ky"]
    chi = ["Than", "Dau", "Tuat", "Hoi", "Ti", "Suu", "Dan", "Meo", "Thin", "Ty", "Ngo", "Mui"]
    ten_am_lich = can[nam % 10] + chi[nam % 12]
    ten_duong_lich = can[(nam + 60) % 10] + chi[(nam + 60) % 12]
    return ten_am_lich,ten_duong_lich

nam = int(input('Nhập năm: '))
am_lich,duong_lich = lichCanChi(nam)
print(nam,am_lich)
print(nam + 60,duong_lich)