lines = []  
with open("test_input.txt") as my_file:
    lines = my_file.readlines()

sumAux = 0

for i in range(len(lines)):
    aux = ""
    firstIndex = None
    lastIndex = None
    for j in range(len(lines[i])):
        breakpoint()
        if(lines[i][j].isnumeric()):
            aux += lines[i][j]
            if firstIndex is None:
                firstIndex = j
            lastIndex = j
        elif(firstIndex is not None and lastIndex is not None):
            breakpoint()
            firstIndex = None
            lastIndex= None
            if "*" in lines[i-1:i+1][j-len(aux):j+len(aux)]:
                sumAux += int(aux)
                

