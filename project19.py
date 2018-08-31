import time

start_time = time.time()
months = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_months = [31,29,31,30,31,30,31,31,30,31,30,31]

day = 0
first_sundays = 0
for i in range(1901,2001):
  leap = i%4
  for j in range(0,12):
    if leap == 0:
      for k in range(1,(leap_months[j])):
        day += 1
        if day % 7 == 0 and k == 1:
          first_sundays += 1
        else:
          first_sundays = first_sundays
    else:
      for l in range(1,(months[j])):
        day += 1
        if day % 7 == 0 and l == 1:
          first_sundays += 1
        else:
          first_sundays = first_sundays
          
print(first_sundays)
print("--- %s seconds ---" % (time.time() - start_time))
