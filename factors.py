#Here is a program I created, inspired by Problem 12, which find the factors of a number entered by the user and tells 
#the user the factors and the total number of factors

def main():
  num = int(input("Input your number:"))
  facs = num_divisors(num)
  print("The Factors of " + str(num) + " are:")
  for each in facs:
    print(each)
  num_factors = len(facs)
  print("In total, the number " + str(num) + " has " + str(num_factors) + " factors")
    
def num_divisors(number):
  fac_array = []
  max_num = number 
  factors = 0 
  factor = 1
  while factor < max_num:
    if number%factor == 0:
      fac_array.append(factor)
      fac_array.append(number/factor)
      factors += 2
      max_num = (number/factor)
      factor += 1
    else:
      factor +=1
  return fac_array
  
main()
