import re

with open('day2-input.txt', 'r') as file:
    total = 0
    for line in file:
        line = line.split(",")
        # Process each string in line
        for sequence in line:
            # The input is range of numbers 11-22 means all numbers from 11 to 22 inclusive, we want the longest 
            # invalid IDs in that range
            sequence = sequence.split("-")
            if len(sequence) != 2:
                continue
            start = int(sequence[0])
            end = int(sequence[1])
            for number in range(start, end + 1):
                num_str = str(number)
                if re.fullmatch(r'(\d+)\1+', num_str):
                    total += number
print(total)


                
