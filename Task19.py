res = 0
b=range(0,10**6)
for i in b:
    res= (3**i)+res
    if res>10**6:
        break
print(res)


res = 0
i=i>=0
while i:
    res= (3**i)+res
    i=i+1
    if res>10**6:
        break
print(res)
