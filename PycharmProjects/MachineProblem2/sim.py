from sys import argv
import sys


predictorType = argv[1]
#print(predictorType)
traceName = argv[len(argv) - 1]
file = open(f"traces/{traceName}", 'r')

correct_predictions = 0
current_prediction = ' '
actual_outcomes = []
predictions_todo = []

while True:
    line = file.readline()

    if not line:
        break

    # print(line)
    words = line.split(' ')

    predictions_todo.append(words[0])
    actual_outcomes.append(words[1].strip())

num_predictions = len(actual_outcomes)
file.close()
# print(actual_outcomes)
# print(predictions_todo)

match predictorType:
    case "smith":
        print("smith debug")
        counter_bits = int(argv[2])
        counter = pow(2, counter_bits - 1)

        for i in range(num_predictions):
            match counter_bits:
                case 1:
                    if counter >= 1:
                        current_prediction = 't'
                    else:
                        current_prediction = 'n'
                case 2:
                    if counter >= 2:
                        current_prediction = 't'
                    else:
                        current_prediction = 'n'
                case 3:
                    if counter >= 4:
                        current_prediction = 't'
                    else:
                        current_prediction = 'n'
                case 4:
                    if counter >= 8:
                        current_prediction = 't'
                    else:
                        current_prediction = 'n'
            if actual_outcomes[i] == current_prediction:
                correct_predictions += 1
            if actual_outcomes[i] == 't':
                if counter_bits == 1 and counter < 1:
                    counter += 1
                elif counter_bits == 2 and counter < 3:
                    counter += 1
                elif counter_bits == 3 and counter < 7:
                    counter += 1
                elif counter_bits == 4 and counter < 15:
                    counter += 1
            elif counter > 0:
                counter -= 1
        misses = num_predictions - correct_predictions
        miss_rate = "{:.2f}".format((misses / num_predictions) * 100)
        print("COMMAND")
        print(f"./sim smith {counter_bits} {traceName}")
        print("OUTPUT")
        print(f"number of predictions: {num_predictions}")
        print(f"number of mispredictions: {misses}")
        print(f"misprediction rate:  {miss_rate}%")
        print(f"FINAL COUNTER CONTENT: {counter}")

    case "gshare":
        #print("gshare debug")
        PC_bits = int(argv[2])  # m
        globalHistoryBits = int(argv[3])  # n
        # (m, n) n no longer = 0
        # initialize GHR to 0, have to do it to n bit length
        GHR = ['0']*globalHistoryBits
        # initialize prediction table.
        predictionTable = {i: 4 for i in range(0, pow(2, PC_bits))}

        for i in range(num_predictions):
            tempInt = int(predictions_todo[i], 16)
            # print(tempInt)

            # convert input address to binary string
            binString = "{:0b}".format(tempInt)
            #print(binString)
            #a little confused at the wording, but we shouldn't trim the PC bits, 000 bits would only give us 8 indices
            # the predictionTable for validation run clearly has 512 indexes that all change.
            # so we should xor the n-bit GHR with an m-bit address.

            #left shift by taking m to 2 bits in the binary string
            tempBin = binString[(PC_bits + 2) * -1:-2]
            # convert to int index
            index = int(tempBin, 2) ^ int("".join(GHR), 2)

            #compare and update prediction table
            if predictionTable[index] >= 4:
                current_prediction = 't'
            else:
                current_prediction = 'n'
            if actual_outcomes[i] == current_prediction:
                correct_predictions += 1
            if actual_outcomes[i] == 't' and predictionTable[index] < 7:
                predictionTable[index] += 1
            elif actual_outcomes[i] == 'n' and predictionTable[index] > 0:
                predictionTable[index] -= 1

            #update GHR

            GHR.pop()
            outcomeBit = '1' if actual_outcomes[i] == 't' else '0'
            GHR.insert(0, outcomeBit)

            #print(GHR)

        #og = sys.stdout
        #sys.stdout = open(f'out_{predictorType}_{traceName}', 'w')

        misses = num_predictions - correct_predictions
        miss_rate = "{:.2f}".format((misses / num_predictions) * 100)
        print("COMMAND")
        print(f"./sim gshare {PC_bits} {globalHistoryBits} {traceName}")
        print("OUTPUT")
        print(f"number of predictions: {num_predictions}")
        print(f"number of mispredictions: {misses}")
        print(f"misprediction rate:  {miss_rate}%")
        print(f"FINAL GSHARE CONTENTS")
        for (key, value) in predictionTable.items():
            print(f"{key} {value}")

        #sys.stdout = og



    case "bimodal":
        # print("bimodal debug")
        PC_bits = int(argv[2])
        # m,n; n=0
        # use a dictionary as a hashtable,
        # if using m pc bits as index, we will need n^2 entries for all possible indices.
        predictionTable = {i: 4 for i in range(0, pow(2, PC_bits))}
        for i in range(num_predictions):
            # convert hex string to int to binary string?
            tempInt = int(predictions_todo[i], 16)
            # print(tempInt)
            binString = "{0:b}".format(tempInt)
            # print(maskString)
            # m+1>>2, PC_bits+1
            tempBin = binString[(PC_bits + 2) * -1:-2]
            index = int(tempBin, 2)
            # print(actual_outcomes[i])
            if predictionTable[index] >= 4:
                current_prediction = 't'
            else:
                current_prediction = 'n'
            if actual_outcomes[i] == current_prediction:
                correct_predictions += 1
            if actual_outcomes[i] == 't' and predictionTable[index] < 7:
                predictionTable[index] += 1
            elif actual_outcomes[i] == 'n' and predictionTable[index] > 0:
                predictionTable[index] -= 1
        misses = num_predictions - correct_predictions
        miss_rate = "{:.2f}".format((misses / num_predictions) * 100)

        #og = sys.stdout
        #sys.stdout = open(f'out_{predictorType}_{traceName}', 'w')

        print("COMMAND")
        print(f"./sim bimodal {PC_bits} {traceName}")
        print("OUTPUT")
        print(f"number of predictions: {num_predictions}")
        print(f"number of mispredictions: {misses}")
        print(f"misprediction rate:  {miss_rate}%")
        print(f"FINAL BIMODAL CONTENTS")
        for (key, value) in predictionTable.items():
            print(f"{key} {value}")

        #sys.stdout = og
    case "hybrid":
        #print("hybrid debug")
        #should have planned out classes, whatever...
        #sim hybrid <K> <M1> <N> <M2>
        chooserBits = int(argv[2])
        gPredictionBits = int(argv[3])
        gHRBits = int(argv[4])
        biPredictionBits = int(argv[5])

        #initiaze tables
        hybridGHR = ['0'] * gHRBits
        chooserTable = {i: 1 for i in range(0, pow(2, chooserBits))}
        gPredictionTable = {i: 4 for i in range(0, pow(2, gPredictionBits))}
        biPredictionTable = {i: 4 for i in range(0, pow(2, biPredictionBits))}

        for i in range(num_predictions):
            #read the address and convert from hex
            tempInt = int(predictions_todo[i], 16)
            #convert to a binary string to make it easier to slice and work with.
            binString = "{:0b}".format(tempInt)

            #There will be a different index process for the chooser table, gshare and bimodal
            #but the process is the same, just the bits taken are different.
            chooseSlice = binString[(chooserBits + 2) * -1:-2]
            gSlice = binString[(gPredictionBits + 2) * -1:-2]
            biSlice = binString[(biPredictionBits + 2) * -1:-2]

            chooseIndex = int(chooseSlice, 2)
            gSliceInt = int(gSlice, 2)
            #I'm removing leading zeros from the GHR at some point
            testStr = ''.join(hybridGHR)
            ghrInt = int(''.join(hybridGHR), 2)
            gIndex = gSliceInt ^ ghrInt
            biIndex = int(biSlice, 2)

            biPrediction = ''
            gPrediction = ''
            #Get predictions from both tables
            if biPredictionTable[biIndex] >= 4:
                biPrediction = 't'
            else:
                biPrediction = 'n'

            if gPredictionTable[gIndex] >= 4:
                gPrediction = 't'
            else:
                gPrediction = 'n'
            #use prediction based on chooser table
            actualOutcome = actual_outcomes[i]
            # compare actual to table predictions, before updating tables.
            #gCorrect = (actualOutcome == gPrediction)
            #biCorrect = (actualOutcome == biPrediction)
            chosenPrediction = ''
            if chooserTable[chooseIndex] >= 2:
                chosenPrediction = gPrediction
                if actualOutcome == 't' and gPredictionTable[gIndex] < 7:
                    gPredictionTable[gIndex] += 1
                elif actualOutcome == 'n' and gPredictionTable[gIndex] > 0:
                    gPredictionTable[gIndex] -= 1

            else:
                chosenPrediction = biPrediction
                if actualOutcome == 't' and biPredictionTable[biIndex] < 7:
                    biPredictionTable[biIndex] += 1
                elif actualOutcome == 'n' and biPredictionTable[biIndex] > 0:
                    biPredictionTable[biIndex] -= 1

            # update GHR
            hybridGHR.pop()
            outcomeBit = '1' if actualOutcome == 't' else '0'
            hybridGHR.insert(0, outcomeBit)

            #update correct predictions
            if chosenPrediction == actualOutcome:
                correct_predictions += 1

            #update chooser table
            if gPrediction != biPrediction:

                if gPrediction == actualOutcome and chooserTable[chooseIndex] < 3:
                    chooserTable[chooseIndex] += 1
                elif chooserTable[chooseIndex] > 0:
                    chooserTable[chooseIndex] -= 1

        misses = num_predictions - correct_predictions
        miss_rate = "{:.2f}".format((misses / num_predictions) * 100)

        print("COMMAND")
        print(f"./sim hybrid {chooserBits} {gPredictionBits} {gHRBits} {biPredictionBits} {traceName}")
        print("OUTPUT")
        print(f"number of predictions: {num_predictions}")
        print(f"number of mispredictions: {misses}")
        print(f"misprediction rate:  {miss_rate}%")
        print(f"FINAL CHOOSER CONTENTS")

        for (key, value) in chooserTable.items():
            print(f"{key} {value}")

        print("FINAL BIMODAL CONTENTS")

        for (key, value) in biPredictionTable.items():
            print(f"{key} {value}")


