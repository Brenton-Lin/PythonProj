from sys import argv
import sys

# The simulator reads a trace file in the following format:
# <hex branch PC> t|n - 302d28 n


# To simulate a smith n-bit counter predictor: sim smith <B> <tracefile>
# To simulate a bimodal predictor: sim bimodal <M2> <tracefile>
# To simulate a gshare predictor: sim gshare <M1> <N> <tracefile>
# To simulate a hybrid predictor: sim hybrid <K> <M1> <N> <M2>

predictorType = argv[1]
print(predictorType)
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
        print("gshare debug")
        prediction_bits = int(argv[2])
        globalHistoryBits = int(argv[3])
        GHR = 0
        tableMask = "1"
        for i in range(1, globalHistoryBits):
            tableMask += '0'
        print(tableMask)
        tableMask += '0'
        for i in range(1, globalHistoryBits):
            tableMask += '1'
        print(tableMask)

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
            #print(tempInt)
            maskString = "{0:b}".format(tempInt)
            #print(maskString)
            # m+1>>2, PC_bits+1
            tempBin = maskString[(PC_bits + 2) * -1:-2]
            index = int(tempBin, 2)
            #print(actual_outcomes[i])
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
        print("hybrid debug")
