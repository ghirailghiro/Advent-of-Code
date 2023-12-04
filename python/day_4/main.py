lines = [] 
with open("input.txt") as my_file:
    lines = my_file.readlines()

aux_sum = 0
list_mine = []

for line in lines:
    line_splitted = line.replace("\n","").split("|")
    list_of_winning_num = line_splitted[0].split(": ")[1].split(" ")
    count_wins = 0
    for num in list_of_winning_num:
        if(num!="" and len(num) == 1):
            num = " "+num
        if num!="" and num in line_splitted[1]:
            breakpoint()
            count_wins+=1
    
    aux_sum+= int(pow(2,(count_wins-1)))
        #print(f"Game : {line_splitted[0]} with {count_wins} with auxsum {aux_sum}")
        

print(f"Part 1 Value: {aux_sum}")

print(f"Part 2 Value: {aux_sum}")

