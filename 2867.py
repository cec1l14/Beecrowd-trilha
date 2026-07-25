C = int(input())

for i in range(C): 
    N, M = map(int, input().split())

    pot = N**M

    print(len(str(pot)))