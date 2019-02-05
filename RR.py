n = int(input())
ID = []
for i in range(1,n+1):
    ID.append(i)
At = list(map(int,input().split()))
Bt = list(map(int,input().split()))
TQ = int(input())
R = []
#Bt = [x for _,x in sorted(zip(At,Bt))]
#ID = [x for _,x in sorted(zip(At,ID))]
BT = Bt.copy()
AT = At.copy()
t = 0
Ct = [0]*n
Tat = [0]*n
Wt = [0]*n
Rt = [1000]*n

c=n
while(c>0):
    for i in range(n):
        if(t >= At[i] and Rt[i] == 1000):
            
            R.append(i)
            
    if(t != 0 and Bt[a] > 0):
        R.append(a)
        
    
    if(len(R)==0):
        print("CPU remains idle from " + str(t) + " to " + str(min(At)) + " seconds")
        t = min(At)
    else:
        a = R.pop(0)
        if(Rt[a] == 1000):
            Rt[a] = t - AT[a]
            At[a] = 9999
        if(Bt[a]>TQ):
            t = t + TQ
            print("The process P" + str(ID[a])+ " executes from time " + str(t - TQ) +  " to " + str(t) + " seconds.")
            Bt[a] = Bt[a] - TQ
            
            
        elif(Bt[a] > 0):
            t = t + Bt[a]
            print("The process P" + str(ID[a])+ " executes from time " + str(t - Bt[a]) +  " to " + str(t) + " seconds.")
            Bt[a] = 0
            Ct[a] = t
            At[a] = 9999
            Tat[a] = Ct[a] - AT[a]
            Wt[a] = Tat[a] - BT[a]
            c = c - 1
            
print("PID\tAT\tBT\tCT\tTAT\tWT\tRT")
for i in range(n):
    print(str(ID[i]) + "\t" + str(AT[i]) + "\t" + str(BT[i]) + "\t" + str(Ct[i]) + "\t" + str(Tat[i]) + "\t" + str(Wt[i]) + "\t" + str(Rt[i]))
st = 0
sw = 0
sr = 0
for i in range(n):
    st = st + Tat[i]
    sw = sw + Wt[i]
    sr = sr + Rt[i]
print("Avg TAT:", st/n)
print("Avg WT:", sw/n)
print("Avg RT:",sr/n)


