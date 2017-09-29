#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(product):
  reverse = int(str(product)[::-1])
  if reverse == product:
    return reverse
  else:
    return 0
  
def multiply(a,b):
  product = a*b
  return product
  
def main():
  highest = 0
  a = 100
  b = 100
  while a < 1000 and b <= 1000:
    if b == 1000:
      b = 100
      a +=1
    else:
      product = multiply(a,b)
      r = palindrome(product)
      if r > highest:
        highest = r
        print(highest)
      else:
        highest = highest
      b += 1
           
main()