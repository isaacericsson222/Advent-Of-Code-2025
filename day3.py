with open('day3-input.txt', 'r') as file:
    total = 0
    for line in file:
        line = line.strip()

        k = max(len(line) - 12, 0)
        # how many digits to remove
        stack = []
            
        for ch in line:
            while k > 0 and stack and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        if k > 0:   
            stack = stack[:-k]

        total += int("".join(stack))
        
print(total)
