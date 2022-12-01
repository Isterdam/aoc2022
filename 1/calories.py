with open('in.txt') as f:
    content = f.read()
    elves = [list(map(int, elf.split("\n"))) for elf in content.rstrip().split("\n\n")]
    # Q1
    calories = list(map(sum, elves))
    print(max(calories))
    # Q2
    calories.sort()
    print(sum(calories[-3:]))