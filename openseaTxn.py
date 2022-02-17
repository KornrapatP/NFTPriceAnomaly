import csv
import json
from web3 import Web3

alchemy = "https://eth-mainnet.alchemyapi.io/v2/D-UbUrIYYmbZldDPY-Mr7dCFv7r-nu9O"
web3 = Web3(Web3.HTTPProvider(alchemy))
with open('ABI/opensea.json') as f:
    abi = json.load(f)
contract = web3.eth.contract(address="0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b", abi=abi)
with open('openseaTransactions.csv', 'r') as inputFile:
    inputReader = csv.reader(inputFile)
    i=0
    for row in inputReader:
        if row[12] != '1' or row[11] != '0':
            i+=1
    print(i)