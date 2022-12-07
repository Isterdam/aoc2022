lines = open('in.txt').read().splitlines() + ['$']

dirs = {}
curr_dir = []
while len(lines) > 0:
    line = lines[0]
    dir = '/'.join(curr_dir)

    if '$ cd ..' in line:
        curr_dir.pop() # pop dir from stack
    elif '$ cd' in line:
        curr_dir.append(line.split()[2]) # push current dir to stack
    elif '$ ls' in line:
        lines = lines[1:]
        contained_files = []

        while True: # parse all the files inside current dir
            line = lines[0]
            if 'dir' in line:
                contained_files.append(dir+'/'+line.split()[1])
            else:
                contained_files.append(line.split()[0])
            if '$' in lines[1]: # hence + ['$'] to lines on row 1
                break
            lines = lines[1:]

        dirs[dir] = contained_files

    lines = lines[1:]

for k in dirs.keys():
    while '/' in ''.join(dirs[k]): # while dir contains other dirs
        subdirs = []
        for v in dirs[k]:
            if v in dirs.keys():
                subdirs += dirs[v]
            else:
                subdirs += [v]
        dirs[k] = subdirs

sought_dirs_size = 0
deleted_dir_size = 70000000
for k in dirs.keys():
    dirs[k] = sum(list(map(int, dirs[k])))
    if dirs[k] <= 100000:
        sought_dirs_size += dirs[k]
    if 70000000 - dirs['/'] + dirs[k] >= 30000000:
        deleted_dir_size = min(deleted_dir_size, dirs[k])

print(sought_dirs_size) # answer 1
print(deleted_dir_size) # answer 2
