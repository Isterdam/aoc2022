line = open('in.txt').read().strip()

print([i+4 for i in range(len(line)-4) if len(set(line[i:i+4]))==4][0]) # answer 1
print([i+14 for i in range(len(line)-14) if len(set(line[i:i+14]))==14][0]) # answer 2
