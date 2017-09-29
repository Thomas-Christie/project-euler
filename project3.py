#Largest prime factor
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

def prime_factors(number):
  factors = []
  divide = 2
  while number > 1:
    while number % divide == 0:
      factors.append(divide)
      number = number / divide
    divide += 1
  return factors

def main():
  number = int(input("Please enter number: "))
  factors = prime_factors(number)
  print("The prime factors are: ")
  for each in factors:
    print(each)
    
main()