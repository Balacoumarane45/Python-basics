Data = [1,2,3,[5,4,9],10,[5,21,5]]

Big = Data[0]
for i in Data:
    try:
        for j in i:
            if(j > Big):
                Big = j
    except:
        if(i > Big):
                Big = i
print(Big)