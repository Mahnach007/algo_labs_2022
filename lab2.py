
row = [ 2, 2, -2, -2, 1, 1, -1, -1 ]
col = [ -1, 1, 1, -1, 2, -2, 2, -2 ]


def DFS(board_size, start, destination ):
    
    teasted = [[False]*board_size for i in range(board_size)]

    
    steps = [start+[0]]

    while True:
        next_steps = []
        
        for step in steps:
            for i in range(len(row)):
                x,y = step[0] + row[i], step[1] + col[i]

                if [x,y] == destination:
                    return step[2]+1
                
                if 0 <= x < board_size and 0 <= y < board_size and not teasted[x][y]:
                    next_steps.append([x,y,step[2]+1])
                    teasted[x][y] = True
        
        steps = next_steps


size = int(input("input size: "))
start_x = int(input("input x: "))
start_y = int(input("input y: "))
end_x = int(input("input x: "))
end_y = int(input("input y: "))

result = DFS(size, [start_x, start_y], [end_x, end_y])

print(result)