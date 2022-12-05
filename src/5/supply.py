lines = open('in.txt').read().splitlines()

part1 = False
stacks = [[] for _ in range(len(lines[0][1::4]))]

def move(n, fr, to):
    # only reverse the crates if part 1
    stacks[to] = stacks[fr][0:n][::-1 if part1 else 1] + stacks[to]
    stacks[fr] = stacks[fr][n:]

for line in lines:
    if '[' in line:
        crates = line[1::4]
        for i in range(len(crates)):
            if crates[i] != ' ': stacks[i].append(crates[i])
    elif 'move' in line:
        args = line.split()
        move(int(args[1]), int(args[3])-1, int(args[5])-1)

print(''.join([stack[0] for stack in stacks]))