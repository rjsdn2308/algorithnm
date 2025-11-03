def sum_n(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s

print(sum_n(10)) # 1부터 10까지 합
print(sum_n(100)) # 1부터 100까지 합 

##다른 버전 sum 코드 구현
def sum_n(n):
    return n*(n+1)//2 # 슬래시 '//'는 정수 나눗셈을 의미합니다. 

print(sum_n(10))
print(sum_n(100))

## 알고리즘 연습 실습 문제
n = int(input("n 값을 입력하세요: "))

sum_square = 0

for i in range(1, n+1):
    s=s+i*i
sum_square += i ** 2


print(f"1부터 {n}까지의 합은 [sum_square]입니다.")