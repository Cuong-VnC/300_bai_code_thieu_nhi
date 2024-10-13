'''
Bài 30: Viết chương trình nhập lãi xuất năm r (%), tiền vốn p 
và thời hạn gởi tiền n(năm). Mỗi trị nhập phải cách nhau bởi
dấu “,”. In ra vốn tích lũy a của từng năm.Chương trình có
kiểm tra nhập thiếu hoặc nhập lỗi.
'''
def tinh_von_tich_luy(lai_suat_nam, tien_von, so_nam):
    von_tich_luy = [tien_von]
    for _ in range(so_nam):
        tien_lai = tien_von * (1 + lai_suat_nam) ** so_nam
        tien_von += tien_lai
        von_tich_luy.append(tien_von)
    return von_tich_luy

if __name__ == "__main__":
  while True:
    try:
      # Nhập, kiểm tra lỗi
     
      lai_suat_nam = float(input('NHập laic suất năm: '))
      tien_von = float(input('Nhạp tiền vồn : '))
      so_nam = int(input("NHập số năm: "))

      # Kiểm tra giá trị hợp lệ
      if lai_suat_nam < 0 or tien_von <= 0 or so_nam <= 0:
        raise ValueError("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại!")

      # Tính và in kết quả
      ket_qua = tinh_von_tich_luy(lai_suat_nam, tien_von, so_nam)
      for nam, von in enumerate(ket_qua, start=1):
        print(f"Năm {nam}: {von:.2f}")
      break  # Thoát khỏi vòng lặp nếu nhập liệu thành công

    except ValueError as e:
      print(f"Lỗi: {e}")