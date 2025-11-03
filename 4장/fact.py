def fact(n):
    f =1 
    for i in range(1, n+1):
        f = f * i
    return f

print(fact(1))
print(fact(5))
print(fact(10))

# 연속한 숫자의 곱을 구하는 알고리즘
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))

# 연속한 숫자의 합을 구하는 알고리즘
def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1) + n

print(sum_n(10))
print(sum_n(100))

# 최댓값 구하기
def find_max(a, n):
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]
    
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))

# 최대공약수 구하기
def gcd(a, b):
    i = min(a, b) # 두 수 중에서 최솟값을 구하는 파이썬 함수
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))

# 최대공약수 구하기 2번째 방법 
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))

# 알고리즘 연습 문제(10872)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

n=int(input())
print(fact(n))

