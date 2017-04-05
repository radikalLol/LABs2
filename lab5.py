fname = input("Имя файла: ")
if len(fname) == 0:
    fname = 'mbox.txt'
fh = open(fname, 'r')
count = 0
tot = 0
ans = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[21:])
    tot = num + tot
ans = tot / count
print("Среднее: "), ans
