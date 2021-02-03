a = [1]

n = int(input("please entre your number"))

for i in range(1,n):
    if (i==1):
        continue
    if i>len(a):
        for c in range(i):
            a.append(i)
        continue
    for b in range(a[i-1]):
        a.append(i)
                       

print(a)