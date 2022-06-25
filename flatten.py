firstList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lastList = []

def flatten(n):
    for i in n:
        #instance
        if isinstance(i,list):
            flatten(i)
        else:
            lastList.append(i)

flatten(firstList)
print(lastList)
