n = input()
ls = input().split()
m = input()
cur = input().split()
print('Missed students: ')

for i in ls:
  ok = 0
  for j in cur:
    if i == j:
      ok = 1
      break
  if ok == 0:
    print('- ' + i)
print('Not in the group: ')

for i in cur:
  ok = 0
  for j in ls:
    if i == j:
      ok = 1
      break
  if ok == 0:
    print('- ' + i)