with open('day5-input.txt', 'r') as file:
    total = 0
    ranges = []
    i = 0
    dataBlocks = file.read().split("\n\n")
    for block in dataBlocks:
        i += 1
        lines = block.split("\n")
        # parse first block
        if i == 1:
            for line in lines:
                line = line.strip()
                #keep track of ranges by collecting them in an array
                parts = line.split("-")
                ranges.append( (int(parts[0]), int(parts[1])) )
        if i == 2:
            print(ranges)
            for line in lines:
                print(line)
                line = line.strip()
                if line == '':
                    break
                num = int(line)
                for r in ranges:
                    if num >= r[0] and num <= r[1]:
                        total += 1
                        break
        

print(total)
