num = 2
for i in range(1,1000):
    num = num*2

number = str(num)
total = 0
for digit in number:
    total += int(digit)

print(total)
