import csv
import json

def flag(arrayOfSet, curBlocknum, fromAd, toAd):
    for seta in arrayOfSet:
        if curBlocknum>=seta[0] and curBlocknum<=seta[1] and fromAd in seta[2] and toAd in seta[2]:
            return True
    return False

arSet = []
with open('COOLSwashTradeCandidates_12hours.csv', 'r') as inputFile:
    inputReader = csv.reader(inputFile)
    for row in inputReader:
        a = []
        a.append(int(row[0]))
        a.append(int(row[1]))
        a.append(set((row[2]).strip('][').split(',')))
        arSet.append(a)

with open('COOLStokensProcessedNx2.csv', 'r') as inputFile:
        inputReader = csv.reader(inputFile)
        with open('COOLStokensProcessedNx2Flag12.csv', 'w') as outputFile:
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(['from', 'to', 'tokenId', 'blockNumber', 'transactionIndex', 'transactionHash', 'ETH', 'isOpensea', 'isSenderContract', 'isRecceiverContract', 'pSale', 'median1000', 'bPR', 'sPR', 'bDG', 'sDG', 'wash'])
            for row in inputReader:
                if row[0] == 'from':
                    continue
                flagVal = 1 if flag(arSet, int(row[3]), row[0], row[1]) else 0
                outputWriter.writerow(row + [flagVal])
