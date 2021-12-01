""" DEL 1 """
depths = []
prevDepth = 0

numIncreased = 0
numDecreased = 0

with open("input.txt") as f:
    for line in f:
        depths.append(int(line.strip()))

# with a list of depths, determine how many succeeding depths are bigger than the prev one
for i in range(len(depths)):
    if i == 0:
        prevDepth = depths[i]
        continue

    if depths[i] > prevDepth:
        numIncreased += 1
    elif depths[i] < prevDepth:
        numDecreased += 1
    prevDepth = depths[i]

# print(numIncreased)
# print(numDecreased)

""" DEL 2 """
prevDepthSum = 0
numIncreased = 0
numDecreased = 0
# sum three consecutive depths, and compare as before
for i in range(len(depths)):
    if i == 0:
        prevDepthSum = depths[i] + depths[i+1] + depths[i+2]
        continue
    
    # stop when we're out of range
    try:
        sum = depths[i] + depths[i+1] + depths[i+2]
        if sum > prevDepthSum:
            numIncreased += 1
        elif sum < prevDepthSum:
            numDecreased += 1
        prevDepthSum = sum
    except IndexError:
        break 

print(numIncreased)
print(numDecreased)
