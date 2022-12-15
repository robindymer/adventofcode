""" DEL 1 """
codes = []
with open("3_input.txt") as f:
    for line in f:
        k = line.strip()
        codes.append(k)

ones = 0
zeros = 0
data = [0,0,0,0,0,0,0,0,0,0,0,0]
tot = [0,0,0,0,0,0,0,0,0,0,0,0]
for code in codes:
    x = [int(a) for a in str(code)]
    for i in range(len(x)):
        data[i] += x[i] # keep track of 1:s
        tot[i] += 1 # keep track of total digits => zeros

gamma = []
epsilon = []

for i in range(len(data)):
    if data[i] > (tot[i] - data[i]):
        # print(tot[i] - data[i])
        gamma.append('1')
        epsilon.append('0')
    else:
        # print("Zero dominating: " + str(data[i]) + " vs " + str(tot[i] - data[i]))
        gamma.append('0')
        epsilon.append('1')

zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(data)):
    zeros[i] = tot[i] - data[i]

bingamma = ''.join(gamma)
binepsilon = ''.join(epsilon)
print(bingamma)
print(binepsilon)
# power consumtion = a * b = c

""" DEL 2 i ny fil """