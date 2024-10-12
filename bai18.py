'''Bài 18: Viết chương trình nhập vào số giờ, xuất ra số 
tương đương tính theo tuần,theo ngày và theo giờ.
'''
def gio_sang_tuan_ngay_gio(so_gio):
    so_tuan = so_gio // (7*24)
    so_gio_con_lai = so_gio % (7*24)
    so_ngay = so_gio_con_lai // 24
    so_gio = so_gio_con_lai % 24
    return so_tuan, so_ngay, so_gio
so_gio = int(input("Nhập số giờ: "))
print(f"{so_gio} giờ tương đương với:")
so_tuan, so_ngay, so_gio =gio_sang_tuan_ngay_gio(so_gio) 
print(f"- {so_tuan} tuần- {so_ngay} ngày- {so_gio} giờ")