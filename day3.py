import os
import re

f=open('day3.txt','r')
text=f.read()

pattern=r"mul\((\d{1,3}),(\d{1,3})\)"

ans=re.findall(pattern,text)
# print(ans)

total=0
for i in ans:
    total+=int(i[0])*int(i[1])

# print(total)
# print(text)

##PART 2
pattern=r"mul\((\d{1,3}),(\d{1,3})\)"
do=r"do\(\)"
dont=r"don't\(\)"

ans=re.findall(f'({do}|{dont}|{pattern})',text)
# print(ans)
total_sum=0
mul_check=True

for i in ans:
    if i[0]=='do()':
        mul_check=True
    elif i[0]=="don't()":
        mul_check=False
    elif i[0].startswith("mul(") and mul_check:
        match=re.match(r"mul\((\d{1,3}),(\d{1,3})\)", i[0])
        if match:
            x=int(match.group(1))
            y=int(match.group(2))
            total_sum+=x*y

print(total_sum)