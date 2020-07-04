a = input()
arr = input().split()
ok = 1

for i in range(len(arr)):
  for j in range(len(arr)):
    if i != j and arr[i] == arr[j] and ok == 1:
      print('NO')
      ok = 0
      break

if ok :
  print(' YES')