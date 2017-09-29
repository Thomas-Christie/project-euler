#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divide(n):
  b = n%19
  c = n%18
  d = n%17
  e = n%16
  f = n%15
  g = n%14
  h = n%13
  i = n%12
  j = n%11
  total = b+c+d+e+f+g+h+i+j
  if total == 0:
    return True
  else:
    return False
  
def main():
  number=20
  divisible=False
  while divisible==False:
    divisible = divide(number)
    if divisible == True:
      print(number)
    else:
      number+=20
      
main()
