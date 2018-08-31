#Problem 14 - Largest Collatz Sequence

longest = 0
long_num = 0
i = 1
for i in range(1,1000000):
    coll_len = 0
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n/2
            coll_len += 1
        else:
            n = 3*n + 1
            coll_len += 1
    if coll_len > longest:
        longest = coll_len + 1
        long_num = i
        n = 1
    else:
        longest = longest
    
print(long_num)
