firstList = [[1, 2], [3, 4], [5, 6, 7]]
firstList = firstList[::-1]
for i in range(len(firstList)):
    firstList[i]=firstList[i][::-1]
print(firstList)
