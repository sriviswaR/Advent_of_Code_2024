import os

f=open('day1.txt','r')
text=f.readlines()

# print(len(text))
l1=[]
l2=[]

for i in range(len(text)):
    ans=text[i].split(' ')
    l1.append(int(ans[0]))
    l2.append(int(ans[3]))

l1.sort()
l2.sort()

answer1=0

for i in range(len(l1)):
    answer1+=abs(int(l1[i])-int(l2[i]))
print(answer1)
dict2={}

for i in range(len(l2)):
    if l2[i] in dict2:
        dict2[l2[i]]+=1
    else:
        dict2[l2[i]]=1

answer=0
for i in l1:
    if i in dict2.keys():
        answer+=i*(dict2[i])

# print(dict2)

print(answer)
