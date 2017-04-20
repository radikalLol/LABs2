#output:
#Average spam confidence: 0.750718518519

# Updated assignment asks users to not use sum() function or variable name in their solution
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox.txt'
fh = open(fname, 'r')
count = 0
tot = 0
ans = 0
l = []
dct = {}
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
for line in fh:
   if line.startswith("Author:"):
       line = line.rstrip().split(':')[1].lstrip()
       if line in dct:
           dct[line] += 1
       else:
           dct[line] = 1
