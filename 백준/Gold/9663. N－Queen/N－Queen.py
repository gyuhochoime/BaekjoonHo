import sys
n = int(sys.stdin.readline())
def dfs(a):
    global cnt
    if a == n:
        cnt += 1
        return
    for i in range(n):
        if visited_1[i] == visited_2[a+i] == visited_3[a-i] == 0:
            visited_1[i] = visited_2[a+i] = visited_3[a-i] = 1
            dfs(a + 1)
            visited_1[i] = visited_2[a+i] = visited_3[a-i] = 0
cnt = 0
visited_1 = [0] * n
visited_2 = [0] * (2 * n)
visited_3 = [0] * (2 * n)
dfs(0)
print(cnt)
