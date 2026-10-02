import csv

def main():

    greedyAlgorithm()

    
def greedyAlgorithm():

    #print("Main program")

    filePath = "../Q3_sequence_main.csv"

    tempList = readfile(filePath)

    #print(DataList)

    sponsorsList = createTable(tempList)


    total = 0

    tempList = sponsorsList.copy()

    while len(tempList) != 0:

        max_value = max(tempList)
        max_index = tempList.index(max_value)
        print("Sponsor value:", max_value)

        total += max_value

        if max_index + 1 <= len(tempList): 
            del tempList[max_index +1 ]

        del tempList[max_index]

        if max_index - 1 >= 0 :
            del tempList[max_index -1]

    print("Total is ", total)



def createTable(tempList):

    tableList = []

    for x in tempList:
        tableList.append(int(x[2]))


    # print(tableList)

    return tableList





def readfile(fileName):

    #print("Reading from file")
    rawList = []

    with open(fileName, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rawList.append(row)

    
    del rawList[0]

    return rawList

        
if __name__ == "__main__":
    #print("Starting program")
    main()
