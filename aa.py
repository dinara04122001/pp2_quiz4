a = int(input()) # ok
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b + 1) :
  if i % d == c:
    print(i)