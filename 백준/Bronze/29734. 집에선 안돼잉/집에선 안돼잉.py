import sys
home, dok = map(int, sys.stdin.readline().rstrip().split())
gt, st = map(int, sys.stdin.readline().rstrip().split())
hm = home // 8
hn = home % 8
dm = dok // 8
dn = dok % 8
ht = dt = 0
if hn == 0:
    ht = home + st * (hm - 1)
else:
    ht = home + st * (hm)
if dn == 0:
    dt = dok + gt * (2 * dm - 1) + st * (dm - 1)
else:
    dt = dok + gt * (2 * dm + 1) + st * dm
if min(ht, dt) == ht:
    print("Zip")
    print(ht)
else:
    print("Dok")
    print(dt)
