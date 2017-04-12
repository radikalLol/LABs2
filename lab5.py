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

for line in fh:
 if not line.startswith("Author:"): continue
 dct = line
if line == dct:
   dct[line] += 1
   print("%s: %s", dct, dct[line])
