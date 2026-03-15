import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num_li = list(map(int, input().split()))
num_li.sort()
cnt = 0

def find(num, idx):
    global cnt
    if num == s:
        cnt+=1
    if idx == n:
        return
    
    for i in range(idx, n):
        find(num+num_li[i], i + 1)
    
for i in range(n):
    find(num_li[i] ,i+1)
    
print(cnt)

