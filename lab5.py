#output:
#Average spam confidence: 0.750718518519

# Updated assignment asks users to not use sum() function or variable name in their solution
# Use the file name mbox-short.txt as the file name
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

fname = input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox.txt'
fh = open(fname, 'r')
count = 0
tot = 0
ans = 0
l = []

for line in fh:
      if not line.startswith("X-DSPAM-Confidence:") : continue
      count = count + 1
      o = line.split()
for i in o:
 try:
  k = float(i)
  l.append(k)
 except:
     pass
 num = map(float, l)
tot = k + tot
ans = tot / count
print("Average spam confidence: ", ans)


import collections
fname = input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox.txt'
fh = open(fname, 'r')
dct = {}
spam = {}
for line in fh:
   if line.startswith("Author:"):
       line = line.rstrip().split(':')[1].lstrip()
       if line in dct:
           dct[line] += 1
       else:
           dct[line] = 1

def fc(spam):
       spam = str(dct)
       spam = spam.split(',')
       for line in spam:
           spam = line.split(':')
           if int(spam[1]) > 90:
            return spam[0]

print("spamers:", fc(spam))

plt.bar(range(len(dct)), dct.values(), align='center')
plt.show()
