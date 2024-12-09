import os
#import re
from collections import deque,defaultdict
from copy import deepcopy

f=open('day5.txt','r')
text=f.read()

#print(text)

rules_part,updates_part=text.strip().split("\n\n")

rules=[tuple(map(int,line.split('|'))) for line in rules_part.splitlines()]
updates=[list(map(int,line.split(','))) for line in updates_part.splitlines()]

#print(updates)


def graph_build(rule,update):
    graph=defaultdict(list)
    in_deg=defaultdict(int)

    pages_update=set(update)
    filtering_rules=[rule for rule in rules if rule[0] in pages_update and rule[1] in pages_update]
    
    for x,y in filtering_rules:
        graph[x].append(y)
        in_deg[y]+=1
        if x not in in_deg:
            in_deg[x] = 0
    return graph,in_deg

#Performing topo sort here
def sorting(update,graph,in_deg):
    queue = deque([node for node in update if in_deg[node]==0])
    sort_order=[]
    
    while queue:
        node=queue.popleft()
        sort_order.append(node)
        for i in graph[node]:
            in_deg[i]-=1
            if in_deg[i] == 0:
                queue.append(i)
    
    return sort_order==update

midsum=0

for update in updates:
        graph,in_deg=graph_build(rules,update)
        if sorting(update,graph,in_deg):
            midsum+=update[len(update)//2]

print(midsum)

#PART 2
def sorting_2(update,graph,in_deg):
    queue = deque([node for node in update if in_deg[node]==0])
    sort_order=[]
    
    while queue:
        node=queue.popleft()
        sort_order.append(node)
        for i in graph[node]:
            in_deg[i]-=1
            if in_deg[i] == 0:
                queue.append(i)
    
    return sort_order

midsum_incorrect=0
for update in updates:
        graph,in_deg=graph_build(rules,update)
        if not sorting(update,graph,deepcopy(in_deg)):
            correct_order=sorting_2(update,graph,deepcopy(in_deg))
            print(correct_order)
            midsum_incorrect+=correct_order[len(correct_order)//2]
print(midsum_incorrect)