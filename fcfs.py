n = int(input())
At = list(map(int,input().split()))
Bt = list(map(int,input().split()))
Q = []
for i in range(1,n+1):
    Q.append(i)
c = n
Ct = n*[0]
Tat = n*[0]
Wt = n*[0]
AT = At.copy()
BT = Bt.copy()
t = 0
while(c>0):
    if(min(At)<=t):
        m = At.index(min(At))
        t = t + Bt[m]
        print("The process P" + str(m+1) + " executes from " + str(t-Bt[m]) + " seconds to " + str(t) + " seconds" )
        Ct[m] = t
        Tat[m] = Ct[m] - At[m]
        Wt[m] = Tat[m] - Bt[m]
        At[m] = 9999
        c = c - 1
    else:
        m = At.index(min(At))
        print("Cpu remains idle from " + str(t) + " seconds to " + str(At[m]) + " seconds")
        t = At[m]
print("PID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(str(Q[i]) + "\t" + str(AT[i]) + "\t" + str(BT[i]) + "\t" + str(Ct[i]) + "\t" + str(Tat[i]) + "\t" + str(Wt[i]))
st = 0
sw = 0
for i in range(n):
    st = st + Tat[i]
    sw = sw + Wt[i]
print("Avg TAT:", st/n)
print("Avg WT:", sw/n)