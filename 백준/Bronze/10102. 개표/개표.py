import sys
n = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip())
aud = {"A": 0, "B": 0}
for i in arr:
    if i == "A":
        aud["A"] += 1
    elif i == "B":
        aud["B"] += 1
if aud["A"] > aud["B"]:
    print("A")
elif aud["A"] == aud["B"]:
    print("Tie")
elif aud["A"] < aud["B"]:
    print("B")
