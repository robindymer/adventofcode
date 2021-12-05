# ta fram typvärdet
# ta bort de övriga
# repetera till enbart en är kvar

codes = []
with open("3_input.txt") as f:
    for line in f:
        codes.append(line.strip())

filteredList = []
for code in codes:
    code = [int(a) for a in str(code)]
    filteredList.append(code)

print(len(filteredList))

i = 0;

while len(filteredList) > 1:
    ones = 0
    zeros = 0
    codeSplitted = []
    for code in filteredList:
        codeSplitted.append(code)
        if code[i] == 1:
            ones += 1
        else:
            zeros += 1
    # print(ones)
    # print(zeros)

    filteredList = []
    if ones >= zeros:
        filtered = filter(lambda n: n[i] == 1, codeSplitted)
        filteredList.append(list(filtered))
    elif ones < zeros:
        filtered = filter(lambda n: n[i] == 0, codeSplitted)
        filteredList.append(list(filtered))
    filteredList = filteredList[0]
    print(len(filteredList))
    i += 1

print(filteredList)

filteredList = []
for code in codes:
    code = [int(a) for a in str(code)]
    filteredList.append(code)

print(len(filteredList))

i = 0;

while len(filteredList) > 1:
    ones = 0
    zeros = 0
    codeSplitted = []
    for code in filteredList:
        codeSplitted.append(code)
        if code[i] == 1:
            ones += 1
        else:
            zeros += 1
    # print(ones)
    # print(zeros)

    filteredList = []
    if ones >= zeros:
        filtered = filter(lambda n: n[i] == 0, codeSplitted)
        filteredList.append(list(filtered))
    elif ones < zeros:
        filtered = filter(lambda n: n[i] == 1, codeSplitted)
        filteredList.append(list(filtered))
    filteredList = filteredList[0]
    print(len(filteredList))
    i += 1

print(filteredList[0])

# print(ones)
# print(zeros)