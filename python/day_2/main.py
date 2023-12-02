lines = []  
with open("input.txt") as my_file:
    lines = my_file.readlines()

red_limit = 12
green_limit = 13
blue_limit = 14

def doLine(line):
    line = line.replace('\n', '')
    runs = line.split('; ')
    runs_and_game = runs[0].split(': ')
    runs[0] = runs_and_game[1]
    runs = {"GameNumber": int(runs_and_game[0].split(" ")[1]), "Runs": runs}
    return runs

def doRun(run):
    runSplitted = run.split(', ')
    return runSplitted

def isRunValid(value, limit):
    return value <= limit

countValidRuns = 0

for line in lines:
    flagValid = True
    runs = doLine(line)
    for run in runs["Runs"]:
        runSplitted = doRun(run)
        for step in runSplitted:
            singleStep = step.split(' ')
            if singleStep[1] == 'red':
                if (not isRunValid(int(singleStep[0]), red_limit)):
                    flagValid = False
            elif singleStep[1] == 'green':
                if (not isRunValid(int(singleStep[0]), green_limit)):
                    flagValid = False
            elif singleStep[1] == 'blue':
                if (not isRunValid(int(singleStep[0]), blue_limit)):
                    flagValid = False
            else:
                #throw exception and stop the program
                print('Invalid color')
    if flagValid:
        countValidRuns += runs['GameNumber']

print(f"Part 1 Value: {countValidRuns}")


countValidRuns = 0

for line in lines:
    red_limit = 0
    green_limit = 0
    blue_limit = 0
    flagValid = True
    runs = doLine(line)
    for run in runs["Runs"]:
        runSplitted = doRun(run)
        for step in runSplitted:
            singleStep = step.split(' ')
            if singleStep[1] == 'red':
                if (not isRunValid(int(singleStep[0]), red_limit)):
                    red_limit = int(singleStep[0])
            elif singleStep[1] == 'green':
                if (not isRunValid(int(singleStep[0]), green_limit)):
                    green_limit = int(singleStep[0])
            elif singleStep[1] == 'blue':
                if (not isRunValid(int(singleStep[0]), blue_limit)):
                    blue_limit = int(singleStep[0])
            else:
                #throw exception and stop the program
                print('Invalid color')
    countValidRuns += red_limit*green_limit*blue_limit

print(f"Part 2 Value: {countValidRuns}")
