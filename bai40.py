'''
Bài 40: Tìm các bộ (trâu đứng, trâu nằm, trâu già) thỏa mãn bài toán cổ:

                    Trăm trâu ăn trăm bó cỏ
                    Trâu đứng ăn năm
                    Trâu nằm ăn ba
                    Lụ khụ trâu già
                    Ba con một bó

        Thử tìm cách giảm số vòng lặp khi tính toán xuống.
'''
def tram_trau_tram_co():
    for i in range(1,101):  # Số trâu đứng
        for j in range(1,101 - i):  # Số trâu nằm
            k = 100 - i - j  # Số trâu già
            if (5*i + 3*j + k/3 == 100):
                print(f"số trâu đứng:{i}\nsố trâu nằm:{j}\nsố trâu già:{k}\n")

tram_trau_tram_co()