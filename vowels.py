string=input()
V=['a','e','i','o','u']
if string.isalpha():
  if string in V:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
