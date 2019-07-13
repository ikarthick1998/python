num=int(input())
if num==2:
  print('yes')
elif num>0:
  for i in range(2,num):
    if num%i==0:
      print('no')
      break
  else:
      print('yes')
