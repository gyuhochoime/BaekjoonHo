import sys
n = sys.stdin.readline().rstrip()
if n.startswith('"') and n.endswith('"') and n.count('"') == 2 and len(n) > 2:
    print(n[1:-1])
else:
    print("CE")
