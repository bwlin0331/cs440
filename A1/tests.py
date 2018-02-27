import csv
import os
import math
import time
from mg2 import *

def main():
    #running aStar tests on all 50 testcases
    # for i in range(50):
        #normal
        # test(str(i+1))
        # time.sleep(1)
        #highg
        # print(test(str(i+1), "highg"))
        # time.sleep(5)
        #lowg
        # test(str(i+1), "lowg")
        # time.sleep(1)
        #back
        # test(str(i+1), "back")
        # time.sleep(1)
        #adaptive
        # test(str(i+1), "adaptive")
        # time.sleep(1)
    # while True:
    testNum = input("Please specify testcase to perform A* on (1-50): ")
    print(test(str(testNum)),"adaptive")

def combine():
    dataType = "normal"
    testNum = '1'
    filename = 'data/' + dataType + '/test' + testNum + '.csv'

    for i in range(50):
        normTime = 0.0
        highgTime = 0.0
        lowgTime = 0.0
        backTime = 0.0
        adaptiveTime = 0.0

        testNum = str(i + 1)

        dataType = "normal"
        with open('data/' + dataType + '/test' + testNum + '.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == "DONE":
                    break
                elif row[0] == "FAIL":
                    # normTime = math.inf
                    break
                else:
                    normTime += float(row[2])

        dataType = "highg"
        with open('data/' + dataType + '/test' + testNum + '.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == "DONE":
                    break
                elif row[0] == "FAIL":
                    # highgTime = math.inf
                    break
                else:
                    highgTime += float(row[2])

        dataType = "lowg"
        with open('data/' + dataType + '/test' + testNum + '.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == "DONE":
                    break
                elif row[0] =="FAIL":
                    # lowgTime = math.inf
                    break
                else:
                    lowgTime += float(row[2])

        dataType = "back"
        with open('data/' + dataType + '/test' + testNum + '.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == "DONE":
                    break
                elif row[0] == "FAIL":
                    # backTime = math.inf
                    break
                else:
                    backTime += float(row[2])

        dataType = "adaptive"
        with open('data/' + dataType + '/test' + testNum + '.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == "DONE":
                    break
                elif row[0] == "FAIL":
                    # adaptiveTime = math.inf
                    break
                else:
                    adaptiveTime += float(row[2])

        # print ("the times are as follows: ", normTime, highgTime, lowgTime,\
        #         backTime, adaptiveTime)

        #initial write to file
        filename = "data.csv"

        sigFig = 5
        normTime = round(normTime, sigFig)
        highgTime = round(highgTime, sigFig)
        lowgTime = round(lowgTime, sigFig)
        backTime = round(backTime, sigFig)
        adaptiveTime = round(adaptiveTime, sigFig)
        if i == 0:
        	#cleaning files for record keeping
            try:
        	    os.remove("data.csv")
            except OSError:
        	    pass
            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(['Testcase #', 'RFAS', 'HighG', 'LowG', 'RBAS', 'Adaptive'])
                writer.writerow([testNum, normTime, highgTime, lowgTime, backTime, adaptiveTime])

        else:
            with open(filename, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([testNum, normTime, highgTime, lowgTime, backTime, adaptiveTime])



if __name__ == "__main__":
    main()
    combine()
    print ("All done")
