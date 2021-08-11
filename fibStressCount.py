from datetime import datetime
from datetime import timedelta
from datetime import time

start_time = datetime.now()

nterms = int(input("What's the initial term? "))

nterms += 1

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Give a valid positive number")
elif nterms == 1:
   print("Fibonacci Sequence > ",nterms,":")
   print(n1)
else:
   print("Fibonacci Sequence:")
   while count < nterms:
       print("{} ".format(n1))
       print("")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

def millis():
   dt = datetime.now() - start_time
   ms = int((dt.days * 24 * 60 * 60 + dt.seconds) * 1000 / 1000 + dt.microseconds)
   s = (dt.days * 24 * 60 * 60 + dt.seconds)
   m = dt.microseconds
   return("{}.{}/{}".format(s,m,ms))

nterms -= 1

print("\nInitial term of Fibonacci Sequence:\t\t\t\t\t", nterms)
print("Calculation duration: \t\t\t\t\t\t\t {}\t\t\t\t\t       (Seconds/Milliseconds)".format(millis()))
