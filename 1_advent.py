depths = []
prevDepth = 0

numIncreased = 0
numDecreased = 0

with open("input.txt") as f:
    for line in f:
        depths.append(int(line.strip()))
for i in range(len(depths)):
    if i == 0:
        prevDepth = depths[i]
        continue

    if depths[i] > prevDepth:
        numIncreased += 1
    elif depths[i] < prevDepth:
        numDecreased += 1

print(numIncreased)
print(numDecreased)
