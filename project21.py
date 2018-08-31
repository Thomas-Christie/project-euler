sum_pd = [0]
for i in range(1,10001):
    pd = 0
    for j in range(1,i):
        if i%j == 0:
            pd += j
    sum_pd.append(pd)

pairs = []
i = 1
while i < len(sum_pd):
    num = sum_pd[i]
    if num <= len(sum_pd):
        if sum_pd[num] == i and num != i:
            pairs.append(i)
            pairs.append(num)
    i += 1
sett = set(pairs)

print(sum(sett))
        
        
            
