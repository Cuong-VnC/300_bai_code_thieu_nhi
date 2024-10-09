'''
Bài 6:Viết chương trình nhập vào 3 số nguyên.Hãy in ba số này 
ra màn hình theo thứ tự tăng dần và chỉ dùng tối đa một biến phụ. 
'''
# Tạo hàm theo yêu cầu đề bài
def sap_xep(ns):
    # Tạo vòng lặp để truy xuất từng index phần tữ trong ns
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            if ns[i] > ns[j]:
                ns[i], ns[j] = ns[j], ns[i]
    return ns

# Xử lý ngoại lệ đầu vào
try: 
    # Nhập chuỗi s là số nguyên
    ns = list(map(int, input().split()))
    # Nếu danh sách rỗng
    if len(ns) == 0:
        print('Danh sach rong')
    else:
        print('Dãy sau khi sắp xếp lại!!!\n',*sap_xep(ns))
except ValueError:
    print('Vui long nhap phan tu la cac so thuc!')