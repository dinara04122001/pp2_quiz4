s = input()
x, y = input().split()
x = int(x)
y = int(y)
posx = 0
posy = 0
ok = 1

if posx == x and posy == y and  ok == 1:
    print('Passed')
    ok = 0

for i in range(len(s)):
  if s[i] == 'L' :
    posx -= 1
  if s[i] == 'R' :
    posx += 1
  if s[i] == 'U' :
    posy += 1
  if s[i] == 'D' :
    posy -= 1
  if posx == x and posy == y and  ok == 1:
    print('Passed')
    ok = 0
if ok :
  print('Missed')