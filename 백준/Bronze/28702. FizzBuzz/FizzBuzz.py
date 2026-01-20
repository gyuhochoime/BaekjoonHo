import sys
for i in range(3, 0, -1):
    a = sys.stdin.readline().rstrip()
    if a not in ["FizzBuzz", "Fizz", "Buzz"]:
        ans = int(a) + i
        break
if ans % 15 == 0:
    print("FizzBuzz")
elif ans % 3 == 0:
    print("Fizz")
elif ans % 5 == 0:
    print("Buzz")
else:
    print(ans)
