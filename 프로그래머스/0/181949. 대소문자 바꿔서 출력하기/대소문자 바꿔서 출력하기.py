import sys
str = list(sys.stdin.readline().rstrip())
for i in range(len(str)):
    if ord(str[i]) <= 90:
        str[i] = str[i].lower()
    else:
        str[i] = str[i].upper()
for i in str:
    print(i, end = "")
