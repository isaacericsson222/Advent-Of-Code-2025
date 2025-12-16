with open('day4-input.txt', 'r') as file:
    total = 0
    x = 0
    y = 0
    map = {}

    offsets = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
]
    
    for line in file:
        #use hashmap to mark number of adjacent rolls
        line = line.strip()
        #go character by character
        for x in range(len(line)):
            if line[x] == "@":
                map[(x, y)] = True
        y += 1



    while True:
        for (x, y) in list(map.keys()):
            neighbor_count = 0
            for ox, oy in offsets:
                if (x + ox, y + oy) in map: 
                    neighbor_count += 1

            if (x, y) in map:
                if neighbor_count < 4:
                    total += 1
                    map[(x, y)] = False # flag for removal
    
        #remove flagged
        if (not False in map.values()):
            break
        while (False in map.values()):
            for key in list(map.keys()):
                if map[key] == False:
                    del map[key]
        


print(total)
