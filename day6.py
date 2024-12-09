f=open('E:/Nvolume/avc/day6.txt','r')
text=f.read()

#print(text)
map=text.strip().split("\n")
rows,cols=len(map),len(map[0])
#print(rows,cols)

directions={'^':(-1,0),'v':(1,0),'>':(0,1),'<':(0,-1)}
order=['^','v','>','<']

guard_position=None
guard_direction=None
obstacles=set()
visited=set()

for r in range(rows):
    for c in range(cols):
        char=map[r][c]
        if char in directions:
            guard_position=(r, c)
            guard_direction=char
        elif char=='#':
            obstacles.add((r, c))

visited=set()
visited.add(guard_position)
    
while True:
    dir_row,dir_col=directions[guard_direction]
    next_pos=(guard_position[0]+dir_row,guard_position[1])

    if next_pos[0]<0 or next_pos[0]>=rows or next_pos[1]<0 or next_pos[1]>=cols:
        break
    if next_pos in obstacles:
            curr_idx=order.index(guard_direction)
            guard_direction=order[(curr_idx + 1) % 4]
    else:
        guard_position = next_pos
        visited.add(guard_position)

print(len(visited))