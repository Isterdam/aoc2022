line = open('in.txt').read().strip()

for j in [4, 14]: # answer 1 and 2
    print([i+j for i in range(len(line)-j) if len(set(line[i:i+j]))==j][0])
