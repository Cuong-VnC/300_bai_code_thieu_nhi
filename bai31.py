'''
Bài 31: Viết chương trình in bảng cửu chương từ 2 đến 9 ra màn hình.
'''
for i in range(2,10):
    print(f"bảng nhân {i}")
    for j in range(1,11):
        print(f'{i} * {j} = ',i * j)        