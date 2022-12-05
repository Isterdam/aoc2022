lines = open('in.txt').read().splitlines()

part1 = False
stacks = [[] for _ in range(9)]

def move(n, fr, to):
    # only reverse the crates if part 1
    stacks[to-1] = stacks[fr-1][0:n][::-1 if part1 else 1] + stacks[to-1]
    stacks[fr-1] = stacks[fr-1][n:]

for line in lines:
    if '[' in line:
        j = 1
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[i-j].append(line[i])
            j += 3
    elif 'move' in line:
        args = line.split(' ')
        move(int(args[1]), int(args[3]), int(args[5]))

print(''.join([stack[0] for stack in stacks]))