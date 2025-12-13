import re

with open('day1-input.txt', 'r') as file:
    y = 0
        # Dial starts at 50
    x = 50
    for line in file:
        char = re.findall(r'[LR]', line)
        direction = re.findall(r'\d+', line)
        print(char[0])
        direction = int(direction[0])
        print(direction)
        if char[0] == 'L':
            x -= direction
            if x < 0:
                if x + direction != 0:
                    y += 1
                    print("passed 0")
                x = abs(x)
                while x > 100:
                    if x - 100 != 0:
                        y += 1
                        print("passed 0!")
                    x -= 100
                x = 100 - x
        elif char[0] == 'R':
            x += direction
            while x >= 100:
                if x - 100 != 0:
                    y += 1
                    print("passed 0!")
                x -= 100
        print("x is ", x)
        if x == 0:
            y += 1
    
    print ("number of of turns = ", y)

    file.close()