import os

f=open('day2.txt','r')
text=f.readlines()

store=[]

def issafe(arr):
    arr=list(map(int, arr))
    for i in range(1,len(arr)):
        diff=abs(arr[i]-arr[i-1])

        if diff<1 or diff>3:
            return False

    inc=[]
    dec=[]

    for i in range(len(arr)-1):
        inc.append(arr[i]<arr[i+1])
        dec.append(arr[i]>arr[i+1])
    
    return all(inc) or all(dec)

def issafe2(arr):
    for i in range(len(arr)):
        mod= arr[:i]+arr[i+1:]
        if issafe(mod):
            return True
    return False


for i in text:
    store.append(i.split())

# print(store)
safe=0
safe2=0

for i in store:
    if issafe(i):
        safe+=1
    if issafe2(i):
        safe2+=1

print(safe)
print(safe2)