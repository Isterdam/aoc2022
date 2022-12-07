from collections import defaultdict
import itertools

def def_value():
    return []

lines = open('in.txt').read().splitlines()

dirs = defaultdict(def_value)
curr_dir = []
for line in lines:
    dir = '/'.join(curr_dir)

    if '$ cd ..' == line:
        curr_dir.pop() # pop dir from stack
    elif '$ cd' in line:
        curr_dir.append(line.split()[2]) # push current dir to stack
    elif '$ ls' in line:
        continue
    else:
        if 'dir' in line:
            dirs[dir].append(dir+'/'+line.split()[1])
        else:
            dirs[dir].append(line.split()[0])

for k in dirs.keys():
    while '/' in ''.join(dirs[k]): # while dir contains other dirs
        dirs[k] = list(itertools.chain(*[dirs[v] if v in dirs.keys() else [v] for v in dirs[k]]))
    dirs[k] = sum(list(map(int, dirs[k])))

print(sum([v for v in dirs.values() if v <= 100000])) # answer 1
print(min([v for v in dirs.values() if 70000000 - dirs['/'] + v >= 30000000])) # answer 2