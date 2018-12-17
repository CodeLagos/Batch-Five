# Lottery machine
#MOJEED Sanni, fmojeedsanni@gmail.com, 08086636963
from random import shuffle

lottery = list(range(1,90))
numbers = []
print("MSP lotto")
for i in range (5):
    shuffle(lottery)
    x = lottery.pop()
    numbers.append(x)
print("What are your numbers?")
f = input()
numbers.sort()

print("Your MSP number are:", numbers)
