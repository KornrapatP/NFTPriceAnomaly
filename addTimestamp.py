import requests
import csv
import time
from utils import fetch_all_tokens_and_eth_txn
import utils
from web3 import Web3


# alchemy = "https://eth-mainnet.alchemyapi.io/v2/D-UbUrIYYmbZldDPY-Mr7dCFv7r-nu9O"
alchemy = "https://eth-mainnet.alchemyapi.io/v2/tVrsCCTFkr0wxMmrjkqbOUTfqyF9dvHB"
web3 = Web3(Web3.HTTPProvider(alchemy))
blocktime = {}

for k in ['IRENEDAO', 'BAYC', 'PUNKS', 'COOLS', 'PPG']:
    print(k)
    with open(k+'tokensPaid2.csv', 'r') as inputFile:
        inputReader = csv.reader(inputFile)
        with open(k+'tokensPaidTime.csv', 'w') as outputFile:
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(['timestamp', 'from', 'to', 'tokenId', 'blockNumber', 'transactionIndex', 'transactionHash', 'ETH', 'isOpensea', 'isSenderContract', 'isRecceiverContract'])
            for row in inputReader:
                if row[0] == 'from':
                    continue
                if int(row[3]) in blocktime:
                    times = blocktime[int(row[3])]
                else:
                    times = web3.eth.getBlock(int(row[3])).timestamp
                    blocktime[int(row[3])] = times
                outputWriter.writerow([times] + row)