import time
 
def primes(limit):
    if limit % 2 != 0: limit += 1
    primes = [True] * limit
    primes[0],primes[1] = [None] * 2
    count = 0 
    for ind,val in enumerate(primes):
        if ind <= limit:
            if val == True:
                # sieve out non-primes by multiples of known primes
                primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
    return primes

def tot(list):
    total = 0
    for ind,val in enumerate(list):
        if val == True:
            total += ind
        else:
            total = total
    return total
        
start = time.time()
limit = int(input("Enter Highest Number: "))
list_p = primes(limit)
total = tot(list_p)
elapsed = (time.time() - start)
print(total)
print(elapsed) 
