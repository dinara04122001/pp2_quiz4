a = input().split()
cur = 0
ans = ''
for i in a :
  if len(i) > cur :
    cur = len(i)
    ans = i
print(ans)
print(cur)