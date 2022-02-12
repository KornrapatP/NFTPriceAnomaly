from web3 import Web3
from utils import create_contract
from events import fetch_events
import csv
import json

addresses = {
    "BAYC": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D",
    "PUNKS": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB",
    "COOLS": "0x1A92f7381B9F03921564a437210bB9396471050C",
    "PPG": "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
    "IRENEDAO": "0x13015585932752A8e6Dc24bE6c07c420381AF53d"
}

periods = {
    "BAYC": {'start':12287507, 'end':14149280},
    "PUNKS": {'start':3914495, 'end':14149280},
    "COOLS": {'start':12715198, 'end':14149280},
    "PPG": {'start':12876179, 'end':14149280},
    "IRENEDAO": {'start':14002329, 'end':14149280}
}

alchemy = "https://eth-mainnet.alchemyapi.io/v2/D-UbUrIYYmbZldDPY-Mr7dCFv7r-nu9O"
web3 = Web3(Web3.HTTPProvider(alchemy))

collectionNames = ["PUNKS"]



def getTransfers(collectionName, web3, period):
    if collectionName == 'PUNKS':
        with open('ABI/punks.json') as f:
            abi = json.load(f)
        keys = ['from', 'to', 'punkIndex', 'blockNumber', 'transactionIndex', 'transactionHash']
    else:
        with open('ABI/erc721.json') as f:
            abi = json.load(f)
        keys = ['from', 'to', 'tokenId', 'blockNumber', 'transactionIndex', 'transactionHash']
    mycontract = create_contract(Web3(Web3.HTTPProvider(alchemy)), abi, addresses[collectionName])
    start = period['start']
    end = start + 300
    keep_event = []

    with open('./'+collectionName+'.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        while True:
            if collectionName=='PUNKS':
                e = mycontract.events.PunkTransfer
            else:
                e = mycontract.events.Transfer
            events = list(fetch_events(e,
                          from_block=start, to_block=end))

            # print(f'{lp_name} | Got {len(events)} events ({start}, {end})')
            print((start-period['start'])/(period['end'] - period['start']))

            for ev in events:
                tmp = dict(ev['args'])
                tmp.update(
                    {'blockNumber': ev['blockNumber'], 'transactionHash': ev['transactionHash'], 'transactionIndex': ev['transactionIndex']})
                dict_writer.writerow(tmp)

            if end > period['end']:
                break
            start = end
            end = start + 300


for collectionName in collectionNames:
    getTransfers(collectionName, web3, periods[collectionName])
