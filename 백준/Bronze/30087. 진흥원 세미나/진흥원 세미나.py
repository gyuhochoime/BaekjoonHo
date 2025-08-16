import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a == "Algorithm":
        print(204)
    elif a == "DataAnalysis":
        print(207)
    elif a == "ArtificialIntelligence":
        print(302)
    elif a == "CyberSecurity":
        print("B101")
    elif a == "Network":
        print(303)
    elif a == "Startup":
        print(501)
    elif a == "TestStrategy":
        print(105)
