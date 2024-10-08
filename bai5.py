'''
Bài 5:Viết chương trình nhập voà toạ độ của tam giác ABC và của điểm M.
Xác định điểm M nằm trong,nằm trên cạnh hay nằm ngoài tam giác ABC.
'''
#Tính dieenj tích
def tinh_dt(A, B, C):
    dt = 0.5 * abs((A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1])))
    return dt
#Kiểm tra vị trí
def kt_vi_tri(A, B, C, M):
    S_ABC = tinh_dt(A, B, C)
    S_MAB = tinh_dt(M, A, B)
    S_MBC = tinh_dt(M, B, C)
    S_MAC = tinh_dt(M, A, C)

    if abs(S_MAB + S_MBC + S_MAC) < S_ABC:
        return "M nằm trong tam giác ABC"
    elif S_MAB == 0 or S_MBC == 0 or S_MAC == 0:
        return "M nằm trên cạnh của tam giác ABC"
    else:
        return "M nằm ngoài tam giác ABC"

# Nhập tọa độ các đỉnh
A = [float(x) for x in input("Nhập tọa độ điểm A (x y): ").split()]
B = [float(x) for x in input("Nhập tọa độ điểm B (x y): ").split()]
C = [float(x) for x in input("Nhập tọa độ điểm C (x y): ").split()]
M = [float(x) for x in input("Nhập tọa độ điểm M (x y): ").split()]

#In kết quả
print(kt_vi_tri(A, B, C, M))