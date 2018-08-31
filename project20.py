import time
start_time = time.time()

factorial = 1
total = 0
for i in range(1,101):
  factorial = factorial*i 
factorial = str(factorial)
for digit in factorial:
  total += int(digit)
  
print(total)
print("--- %s seconds ---" % (time.time() - start_time))
