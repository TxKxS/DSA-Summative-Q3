import csv

def main():

    filePath = "../Q3_sequence_main.csv"

    greedyAlgorithm(filePath)

    nonGreedyAlgo(filePath)

    filePath = "../Q3_sequence_selfcheck.csv"
    
    greedyAlgorithm(filePath)
    
    nonGreedyAlgo(filePath)



def nonGreedyAlgo(filePath):

    print("\nNon greedy algorithm")

    
    
    tempList = readfile(filePath)

    sponsorsList = createTable(tempList)


    dp = [0] * len(sponsorsList)

    #Bases Cases
    dp[0] = sponsorsList[0]
    dp[1] = max(sponsorsList[1],sponsorsList[0])

    for i in range(2,len(sponsorsList)):
        dp[i] = max(dp[i-2] + sponsorsList[i] , dp[i -1] )

    print("Max is " , dp[len(dp) -1])
    print(dp)




    
def greedyAlgorithm(filePath):

    print("\nGreedy Algorithm")


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

        if (max_index + 1) < len(tempList): #index is always 1 less than length
            del tempList[max_index +1]

        del tempList[max_index]

        if max_index - 1 >= 0 :
            del tempList[max_index - 1]

    print("Total is ", total)



def createTable(tempList):

    tableList = []

    for x in tempList:
        tableList.append(int(x[2]))

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

def dynamicPrograming():

    filePath = "../Q3_sequence_main.csv"
    
    tempList = readfile(filePath)
    
    
    sponsorsList = createTable(tempList)
    
    total = 0
    
    tempList = sponsorsList.copy()


     

        
if __name__ == "__main__":
    #print("Starting program")
    main()
