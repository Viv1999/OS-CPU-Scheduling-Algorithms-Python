n = int(input())
At = list(map(int,input().split()))
Bt = list(map(int,input().split()))
Pr = list(map(int,input().split()))
ID = []
for i in range(1,n+1):
    ID.append(i)
Bt = [x for _,x in sorted(zip(At,Bt))]
ID = [x for _,x in sorted(zip(At,ID))]
AT = At.copy()
BT = Bt.copy()
stri = input('Enter h for high priority for higher number and l vice versa')
if(stri == 'h'):
    boo = True
    R = [0]*n
else:
    boo = False
    R = [9999]*n
AT = At.copy()
BT = Bt.copy()
Ct = [0]*n
Tat = [0]*n
Wt = [0]*n
t = 0
c = n
Re = [9999]*n
while(c>0):
    for i in range(n):
        if(t >= At[i]):
            R[i] = Pr[i]
    if(boo):
        if(max(R) != 0):
           m = Pr.index(max(R))
        else:
            m = At.index(min(At))
            print("CPU remains idle from " + str(t) + " to " + str(At[m]) + " seconds")
            t =  At[m]
    else:
        if(min(R) != 0):
            m = Pr.index(min(R))
        else:
            m = At.index(min(At))
            print("CPU remains idle from " + str(t) + " to " + str(At[m]) + " seconds")
            t =  At[m]
    if(Re[m]==9999):
        Re[m] = t - AT[m]
    t = t + 1
    Bt[m] = Bt[m] - 1
    if(Bt[m] == 0):
        Ct[m] = t
        Tat[m] = Ct[m] - At[m]
        Wt[m] = Tat[m] - BT[m] 
        At[m] = 9999
        R[m] = 0 if(boo) else 9999
        c = c - 1
    print("The process P" + str(ID[m])+ " executes from time " + str(t - 1) +  " to " + str(t) + " seconds.")
    
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
print("Avg RT:", sr/n)    
    