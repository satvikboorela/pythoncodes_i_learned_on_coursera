import re
fhand= open("sample_data.txt")
x=list()
for line in fhand:
    y= re.findall ('[0-9]+',line)
    x=x+y
sum=0
for z in x:
    sum=sum+ int(z)
print(sum)
