str1=input('')
str2=input('')
count = 0
if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        else:
            count += 1
if count == 1:
    print("yes")
else:
    print("no")
