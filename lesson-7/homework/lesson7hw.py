#Problems
#1. is_prime(n) funksiyasi
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(12))

#2.digit_sum(k) funksiyasi
def digit_sum(k):
    total = list(map(int, str(k)))
    return sum(total)
print(digit_sum(502))

#3. Ikki sonning darajalari
def power_of_two(N):
    current=2
    while current<=N:
        print (current, end=' ')
        current*=2
(power_of_two(20))
