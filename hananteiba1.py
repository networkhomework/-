        d= { }
L1 = ['HTTP','HTTPS','FTP','DNS']
L2 = [80,433,20,53]
for n,m in zip(L1,L2):
    d[n]=m
print(d)
