from web3 import Web3
import utils
import csv

alchemy = "https://eth-mainnet.alchemyapi.io/v2/tVrsCCTFkr0wxMmrjkqbOUTfqyF9dvHB"
web3 = Web3(Web3.HTTPProvider(alchemy))

collectionNames = ["COOLS", "BAYC", "IRENEDAO", "PPG", "PUNKS"]

def convert(collectionName, web3):
    with open(collectionName + 'tokensPaid.csv', 'r') as inputFile:
        inputReader = csv.reader(inputFile)
        with open(collectionName+'tokensPaidETH', 'w') as outputFile:
            outputWriter = csv.writer(outputFile)
            prevRow = None
            for row in inputReader:
                if row[0] == "from":
                    outputWriter.writerow(row + ["priceETH"])
                elif row[0] == "ETH":
                    outputWriter.writerow(prevRow + [utils.convert_all_to_eth(web3, row, int(prevRow[3]))/10e18])
                else:
                    prevRow = row
collectionNames = ['PUNKS']
for collectionName in collectionNames:
    convert(collectionName, web3)
