import time

start_time = time.time()
units = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
tens = {0:0, 1:3 , 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
awkward = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
total = 0

for i in range(1,1000): 
  unit = i%10
  ten = (i//10)%10  
  hundred = i//100
  if i < 10:
    total += units[i]
  elif i >= 10 and i < 20:
    total += awkward[i]
  elif i >= 20 and i <100:
    total += units[unit]
    total += tens[ten]
  elif i % 100 == 0:
    total += 7 #hundred
    total += units[hundred]
  elif i > 100 and i % 100 != 0 and ten != 1:
    total += 3 #and
    total += 7 #hundred
    total += units[unit]
    total += tens[ten]
    total += units[hundred]
  else:
    total += 3 #and
    total += 7 #hundred
    total += units[hundred]
    total += awkward[i%100]
  
total += 11
print(total)
print("--- %s seconds ---" % (time.time() - start_time))
