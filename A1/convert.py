import csv

def main():
    full = []
    # with open('data.csv','r') as csvfile:
    #     reader = csv.reader(csvfile)
    #     print ("here?")
    #     for row in reader:
    #         print('this is here')
    #         print(row[0])
    #         full.append(row)
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            full.append(row)

    f = open("toLatex.txt", 'w')
    for row in full:
        f.write(str(row[0]) + '&' + str(row[1]) + '&' + str(row[2]) + '&' + str(row[3])\
             + '&' + str(row[4]) + '&' +  str(row[5]) + '\\\\\n')

    f.close()

if __name__ =="__main__":
    main()
