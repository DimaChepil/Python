e=0.0001
sum=0
i=2
a=1
while a>e:
    a=i/(i-1)**2
    sum+=a
    i+=1
print(sum)
