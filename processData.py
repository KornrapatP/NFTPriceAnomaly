
import requests
import csv
import time
from utils import fetch_all_tokens_and_eth_txn
import utils
from web3 import Web3
import statistics


alchemy = "https://eth-mainnet.alchemyapi.io/v2/D-UbUrIYYmbZldDPY-Mr7dCFv7r-nu9O"
# alchemy = "https://eth-mainnet.alchemyapi.io/v2/tVrsCCTFkr0wxMmrjkqbOUTfqyF9dvHB"
web3 = Web3(Web3.HTTPProvider(alchemy))

salePrices = []
primarySales = set([])
secondarySales = set([])

for k in ['COOLS']:
    ind = 0
    freq = {}
    with open(k+'tokensPaid2.csv', 'r') as inputFile:
        inputReader = csv.reader(inputFile)
        for row in inputReader:
            freq[(row[4], row[5])] = freq.get((row[4], row[5]),0)+1


    with open(k+'tokensPaid2.csv', 'r') as inputFile:
        inputReader = csv.reader(inputFile)
        with open(k+'tokensProcessed.csv', 'w') as outputFile:
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(['from', 'to', 'tokenId', 'blockNumber', 'transactionIndex', 'transactionHash', 'ETH', 'isOpensea', 'isSenderContract', 'isRecceiverContract', 'pSale', 'median1000'])
            for row in inputReader:
                if row[0]=='from' or row[7]=='0' or row[2]=='7363' or row[2] == '7373':
                    continue
                median = 0
                curBn = int(row[3])
                if len(salePrices)>0:
                    ind = 0
                    for i in range(len(salePrices)):
                        if (salePrices[i][0]>=curBn):
                            ind = i
                            break
                    salePrices = salePrices[ind:]
                    median = statistics.median([i[1] for i in salePrices])
                
                tokenId = int(row[2])
                n=len(primarySales)
                s=len(secondarySales)
                pSale = 0.5/(n+1)+s/(n+1)
                if tokenId not in primarySales and tokenId not in secondarySales:
                    primarySales.add(tokenId)
                elif tokenId in primarySales and tokenId not in secondarySales:
                    primarySales.remove(tokenId)
                    secondarySales.add(tokenId)


                salePrices.append((int(row[3]), float(row[6])/freq[(row[4], row[5])]))
                outputWriter.writerow(row + [pSale, median])
