lines = []  
with open("input.txt") as my_file:
    lines = my_file.readlines()

sumAux = 0
possible_simbols = ["!", "@", "#", "$", "%","^","&","*","(",")","-","+","?","_","=",",","<",">","/"]

for i in range(len(lines)):
    aux = ""
    firstIndex = None
    lastIndex = None
    for j in range(len(lines[i])):
        if(lines[i][j].isnumeric()):
            aux += lines[i][j]
            if firstIndex is None:
                firstIndex = j
            lastIndex = j
        elif(firstIndex is not None and lastIndex is not None):
            preLine = ""
            postLine = ""
            if(firstIndex!=0):
                firstIndex -= 1
            if(lastIndex!=len(lines[i])-1):
                lastIndex +=2
            else:
                lastIndex+=1
            if(i!=0):
                preLine = lines[i-1][firstIndex:lastIndex]
            if(i!=len(lines)-1):
                postLine = lines[i+1][firstIndex:lastIndex] 
            checkLine = preLine + postLine + lines[i][firstIndex:lastIndex]
            if  any([k in checkLine for k in possible_simbols]):
                print(aux)
                sumAux += int(aux)
            aux = ""
            firstIndex = None
            lastIndex= None
                
print(f"Part 1 Value: {sumAux}")


for i in range(len(lines)):
    aux = ""
    firstIndex = None
    lastIndex = None
    for j in range(len(lines[i])):
        if(lines[i][j] == "*"):
            aux += lines[i][j]
            if firstIndex is None:
                firstIndex = j
            lastIndex = j
            preLine = ""
            postLine = ""
            if(firstIndex!=0):
                firstIndex -= 1
            if(lastIndex!=len(lines[i])-1):
                lastIndex +=2
            else:
                lastIndex+=1
            if(i!=0):
                preLine = lines[i-1][firstIndex:lastIndex]
            if(i!=len(lines)-1):
                postLine = lines[i+1][firstIndex:lastIndex] 
            checkLine = preLine + postLine + lines[i][firstIndex:lastIndex]
            if  any([k in checkLine for k in possible_simbols]):
                print(aux)
                sumAux += int(aux)
            aux = ""
            firstIndex = None
            lastIndex= None
                
print(f"Part 2 Value: {sumAux}")

