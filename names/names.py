import time
import os

start_time = time.time()

path = os.path.dirname(os.path.realpath(__file__)) # finds absolute path

f = open(f'{path}/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(f'{path}/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
names = {}

for n1 in names_1:
    names[n1] = n1
   

for n2 in names_2:
    if n2 in names:  # duplicate check
        duplicates.append(n2)  # add


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
