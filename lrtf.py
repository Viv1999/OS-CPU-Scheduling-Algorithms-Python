n = int(input())
ID = []
for i in range(1,n+1):
    ID.append(i)
At = list(map(int,input().split()))
P = list(map(int,input().split()))
Bt = [x for _,x in sorted(zip(At,P))]
ID = [x for _,x in sorted(zip(At,ID))]
AT = At.copy()
BT = Bt.copy()
Ct = [0]*n
Tat = [0]*n
Wt = [0]*n
Re = [1000]*n
t = 0
R = [-1]*n
c=n
while(c>0):
    for i in range(n):
        if(t >= At[i] and R[i]!=-2):
            R[i] = Bt[i]
    if(max(R)>0):
        m = Bt.index(max(R))
        if(Re[m] == 1000):
            Re[m] = t - AT[m]
        t = t + 1
        Bt[m] = Bt[m] - 1
        print("The process P" + str(ID[m])+ " executes from time " + str(t - 1) +  " to " + str(t) + " seconds.")
        if(Bt[m] == 0):
            Ct[m] = t
            R[m] = -2
            Tat[m] = Ct[m] - At[m]
            Wt[m] = Tat[m] - BT[m]
            Bt[m] = -1
            c = c - 1
            At[m] = 9999
    else:
        m = At.index(min(At))
        print("CPU remains idle from " + str(t) + " to " + str(At[m]) + " seconds")
        t = At[m]
print("PID\tAT\tBT\tCT\tTAT\tWT\tRT")
for i in range(n):
    print(str(ID[i]) + "\t" + str(AT[i]) + "\t" + str(BT[i]) + "\t" + str(Ct[i]) + "\t" + str(Tat[i]) + "\t" + str(Wt[i]) + "\t" + str(Re[i]))
st = 0
sw = 0
sr = 0
for i in range(n):
    st = st + Tat[i]
    sw = sw + Wt[i]
    sr = sr + Re[i]
print("Avg TAT:", st/n)
print("Avg WT:", sw/n)
print("Avg RT:",sr/n)