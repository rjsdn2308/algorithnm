def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, to_pos)
        return
    
    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)

print("n = 1")
hanoi(1,1,3,2)
print("n = 2")
hanoi(2,1,3,2)
print("n = 3")
hanoi(3,1,3,2)

# 재귀 호출을 이용한 사각 나선 그리기
import turtle as t

def spiral(sp_len):
    if sp_len <=5:
        return 
    t.forward(sp_len)
    t.right(90)
    spiral(sp_len - 5)

t.speed(0)
spiral(200)
t.hideturtle()
t.done()

# 알고리즘 문제 하노이의 탑 이동 순서 11729
n = int(input())

def hanoi(n, start, end, mid):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, mid, end)
    print(start, end)
    hanoi(n - 1, mid, end, start)

print(2 ** n - 1)
hanoi(n, 1, 3, 2)