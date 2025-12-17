with open('day5-input.txt', 'r') as file:
    total = 0
    ranges = []

    for line in file:
        line = line.strip()
        #keep track of ranges by collecting them in an array
        parts = line.split("-")
        ranges.append( (int(parts[0]), int(parts[1])))

    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]
    for current_start, current_end in ranges[1:]:
        last_merged_start, last_merged_end = merged[-1]

        # Check for overlap and merge if necessary
        if current_start <= last_merged_end:
            merged[-1] = (last_merged_start, max(current_end, last_merged_end))
        else:
            merged.append((current_start, current_end))
        
    for i in range(len(merged)):
        start, end = merged[i]
        total += (end - start + 1)

print(total)
