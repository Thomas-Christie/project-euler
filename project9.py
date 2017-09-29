#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import math

def pythag(a,b,c):
        if a**2 + b**2 == c**2:
            return True
        else:
            return False

for i in range(1,500):
    for j in range(i, 1000-i):
        for k in range(j, 1000-j):
            if i+j+k == 1000:
                if pythag(i,j,k):
                    print(i,j,k)
                    print(i*j*k)
                    
