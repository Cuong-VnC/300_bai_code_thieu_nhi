'''
Bài 42: Từ giả thuyết Goldbach lẻ (odd Goldbach's conjecture) suy ra rằng: một số
nguyên tố n bất kỳ (n > 5) đều có thể biểu diễn bằng tổng của ba số nguyên tố khác.
Viết chương trình kiểm chứng giả thuyết này với n < 1000.
'''
def kt_so_nguyen_to(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def kt_gia_thuyet(limit):
    primes = [num for num in range(1, limit) if kt_so_nguyen_to(num)]
    for n in primes[3:]:  # Bắt đầu từ số nguyên tố thứ 3 (5)
        found = False
        for i in range(1, len(primes)):
            p = primes[i]
            if p > n // 2:
                break
            for j in range(i, len(primes)):
                q = primes[j]
                if p + q >= n:
                    break
                if kt_so_nguyen_to(n - p - q):
                    found = True
                    print(f"{n} = {p} + {q} + {n-p-q}")
                    break
            if found:
                break
        if not found:
            print(f"Không tìm thấy cách biểu diễn {n} thành tổng 3 số nguyên tố")

kt_gia_thuyet(1000)
        
        
        