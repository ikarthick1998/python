a=list(input(""))
for i in range(0,len(a),2):
  b=''.join(a[i+1]+a[i])
  print(b,end='')
