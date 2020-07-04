a, b = input().split()
a = int(a)
b = int(b)
cur = 0

while a <= b :
  cur = cur +1
  a *= 3
  b *= 2
print( cur)