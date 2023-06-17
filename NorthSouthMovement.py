"""
You are standing on an infinite 2D Plane. Assume you are
at the origin(0,0). There are 4 types of queries
1 x -> Move x units in direction you are facing
2 x -> Turn 45 degrees x times to your left
3 x -> Turn 45 degrees x times to your right
4   -> Print X Y D (your x, y coordination & direction)
Direction Map - B - North, F - South

A           B            C
D       your location    E
F           G            H
Input format:
First line is initial location & facing direction
Second line is Q number of queries
3 line onwards are queries
INPUT :-
-3 -6 C
3
4
1 3
4
OUTPUT :-
-3 -6 C
 0 -3 D
"""
rightRotationDirection = ['A', 'B', 'C', 'D', 'E', 'H', 'G', 'F', 'D']
leftRotationDirection = ['H', 'E', 'C', 'B', 'A', 'D', 'F', 'G']

x, y, direction = [t for t in input().split()]
x = int(x)
y = int(y)
queries = int(input())
for i in range(queries):
    line = [t for t in input().split()]
    if len(line) == 4: # It's 4
        print(x, y, direction)
    else:
        firstVal, secondVal = int(line[0]), int(line[1])
        if firstVal == 1: # move in direction you are facing
            move(secondVal)
        elif firstVal == 2: # turn 45 degrees n times to left
            rotate(secondVal, "left")
        elif firstVal == 2: # turn 45 degrees n times to right
            rotate(secondVal, "right")

def rotate(times, rotatingDirection):
    global direction
    times%=8 # It's a cycle of 8 check direction map
    if rotatingDirection == "right":
        matrix = rightRotationDirection
    else:
        matrix = leftRotationDirection
    currentDirectionIndex = matrix.index(direction)
    newDirectionIndex = currentDirectionIndex+times
    if newDirectionIndex>=8:
        newDirectionIndex%=8
    elif newDirectionIndex<0:
        newDirectionIndex+=8
    direction = matrix[newDirectionIndex]

def move(unit):
    global x, y, direction
    if direction =='A':
        x-=unit
        y+=unit
    elif direction =='B':
        y+=unit
    elif direction =='C':
        x+=unit
        y+=unit
    elif direction =='D':
        x-=unit
    elif direction =='E':
        x+=unit
    elif direction =='F':
        x-=unit
        y-=unit
    elif direction =='G':
        y-=unit
    elif direction =='H':
        x+=unit
        y-=unit
