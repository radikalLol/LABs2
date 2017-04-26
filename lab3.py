import sys
string = []

def Poly(element):

   if element == 0:
    return 1/int(element)*3

if __name__ == '__main__' :
  string = sys.argv[1]
  string = string.split('--poly=')
  string = string[1].split(',')

  sum = 0
  for element in string:
    sum += Poly(element)
  print(string)
  print(sum)

