'''
Bài 58: Viết chương trình thực hiện thuật toán sàng Erastosthenes (Sieve of
Erastosthenes) để in ra các số nguyên tố nhỏ hơn số n cho trước (n < 100).
'''

def sieve_of_eratosthenes(n):
    # Tạo một danh sách đánh dấu từ 0 đến n-1
    prime = [True] * n
    prime[0] = prime[1] = False  # 0 và 1 không phải số nguyên tố

    # Bắt đầu sàng từ số 2
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            # Đánh dấu các bội số của i là không nguyên tố
            for j in range(i * i, n, i):
                prime[j] = False

    # Trả về các số nguyên tố
    series_primes = [i for i in range(n) if prime[i]]
    return series_primes

# Nhập số n
n = int(input("Nhập số n (n < 100): "))
if n >= 100:
    print("Vui lòng nhập số nhỏ hơn 100.")
elif n <= 0:
    print("Nhập không đúng định dạng!")
else:
    primes = sieve_of_eratosthenes(n)
    print(f"Các số nguyên tố nhỏ hơn {n} là: {primes}")



    