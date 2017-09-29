#Multiples of 3 and 5
#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

limit = 1000

def check_multiples(limit):
  multiples = []
  for i in range(1,limit):
    if i % 3 == 0:
      multiples.append(i)
    if i % 3 != 0 and i % 5 == 0:
      multiples.append(i)
  return multiples

def sum(multiples):
  total = 0
  for each in multiples:
    total += each
  return total

def main():
  limit = int(input("Please enter limit: "))
  multiples = check_multiples(limit)
  total = sum(multiples)
  print("The sum of the multiples of 3 or 5 below ", limit, " is: ", total)
  
main()