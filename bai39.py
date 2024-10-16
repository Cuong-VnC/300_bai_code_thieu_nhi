'''
Bài 39: Một bộ ba Pythagorean là một bộ ba số tự nhiên a < b < c, thỏa mãn công
thức Pithagoras6: a^2 + b^2 = c^2.
Tìm các bộ ba Pythagorean nhỏ hơn 100 là 3 số nguyên
liên tiếp hoặc 3 số chẵn liên tiếp.
'''
#Hàm kiểm tra điều kiện đề bài
def kiem_tra():
    for i in range(1,100):
        for j in range(1,100):
            for k in range(1,100):
                if (i < j < k) and (i**2 + j**2 == k**2) and (i % 2 == 0) and (j % 2 == 0) and (k % 2 == 0):
                    print(f"({i},{j},{k}): ba số chẵn liên tiếp")
                if (i < j < k) and (i**2 + j**2 == k**2):
                    print(f"({i},{j},{k}: ba số nguyên liên tiếp)")

#gọi hàm
kiem_tra()
                    
                