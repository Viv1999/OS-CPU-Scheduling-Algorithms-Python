n = int(input())
p = []
for i in range(1,n+1):
    p.append(i)
At = list(map(int,input().split()))
Bt = list(map(int,input().split()))
Ct = n*[0]
Tat = n*[0]
Wt = n*[0]
P = [x for _,x in sorted(zip(At,Bt))]
Q = [x for _,x in sorted(zip(At,p))]
BT = P.copy()
At.sort()
ATi = At.copy()
t = 0
c = n
R = n*[9999]
while(c>0):
    for i in range(n):
        if(t >= At[i] and R[i] == 9999):
            R[i] = P[i]
    if(min(R)<9999):
        m = P.index(min(R))
        t = t + P[m]
        Ct[m] = t
        Tat[m] = Ct[m] - At[m]
        Wt[m] = Tat[m] - P[m] 
        At[m] = 9999
        R[m] = 9999
        print("The process P" + str(Q[m])+ " executes from time " + str(t - P[m]) +  " to " + str(t) + " seconds.")
        P[m] = 9999
        c = c - 1
    else:
        m = At.index(min(At))
        print("CPU remains idle from " + str(t) + " to " + str(At[m]) + " seconds")
        t =  At[m]
print("PID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(str(Q[i]) + "\t" + str(ATi[i]) + "\t" + str(BT[i]) + "\t" + str(Ct[i]) + "\t" + str(Tat[i]) + "\t" + str(Wt[i]))
st = 0
sw = 0
for i in range(n):
    st = st + Tat[i]
    sw = sw + Wt[i]
print("Avg TAT:", st/n)
print("Avg WT:", sw/n)