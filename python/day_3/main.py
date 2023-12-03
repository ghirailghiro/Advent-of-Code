lines = []  
with open("test_input.txt") as my_file:
    lines = my_file.readlines()

sumAux = 0
possible_simbols = ["!", "@", "#", "$", "%","^","&","*","(",")","-","+","?","_","=",",","<",">","/"]
'''
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
'''



for i in range(len(lines)):
    aux = ""
    for j in range(len(lines[i])):
        if(lines[i][j] == "*"):
            firstIndex = j
            lastIndex = j
            breakpoint()
            #aux += lines[i][j]
            preLine = ""
            postLine = ""
            if(j!=0):
                firstIndex -= 1
            if(j!=len(lines[i])-1):
                lastIndex +=2
            else:
                lastIndex +=1
            if(i!=0):
                preLine = lines[i-1][firstIndex:lastIndex]
            if(i!=len(lines)-1):
                postLine = lines[i+1][firstIndex:lastIndex] 
            list_of_adjagent_num = []
            auxIntToInsertPost = ""
            auxIntToInsertPre = ""
            if(postLine != ""):
                for k in range(len(lines[i+1])):
                    if(postLine != "" and lines[i][k].isdigit()):
                        auxIntToInsertPost+=lines[i][k]
                    elif(postLine != "" and auxIntToInsertPost!= ""):
                        if(k+len(auxIntToInsertPost)>=lastIndex & k-len(auxIntToInsertPost) <=firstIndex):
                            breakpoint()
                            list_of_adjagent_num.insert(int(auxIntToInsertPost))
                        auxIntToInsertPost = ""
            if(preLine != ""):
                for k in range(len(lines[i-1])):
                    if(preLine != "" and lines[i][k].isdigit()):
                        auxIntToInsertPre+=lines[i][k]
                    elif(preLine != "" and auxIntToInsertPre!= ""):
                        if(k+len(auxIntToInsertPre)>=lastIndex & k-len(auxIntToInsertPre) <=firstIndex):
                            breakpoint()
                            list_of_adjagent_num.insert(int(auxIntToInsertPre))
                        auxIntToInsertPre = ""
                    
                                
            #checkLine = preLine + postLine + lines[i][firstIndex:lastIndex]
            #if  any([k in checkLine for k in possible_simbols]):
            #    print(aux)
            #    sumAux += int(aux)
            #aux = ""
            #firstIndex = None
            #lastIndex= None
                
print(f"Part 2 Value: {sumAux}")

