import requests
import shutil
from web3 import Web3
from utils import create_contract
import json
from os.path import exists

# alchemy = "https://eth-mainnet.alchemyapi.io/v2/D-UbUrIYYmbZldDPY-Mr7dCFv7r-nu9O"
alchemy = "https://eth-mainnet.alchemyapi.io/v2/tVrsCCTFkr0wxMmrjkqbOUTfqyF9dvHB"
web3 = Web3(Web3.HTTPProvider(alchemy))

maxID = {'COOLS': 9941}
addresses = {
    "BAYC": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D",
    "PUNKS": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB",
    "COOLS": "0x1A92f7381B9F03921564a437210bB9396471050C",
    "PPG": "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
    "IRENEDAO": "0x13015585932752A8e6Dc24bE6c07c420381AF53d"
}

with open('ABI/erc721.json') as f:
    abi = json.load(f)
    

for collection, max_id in maxID.items():
    mycontract = create_contract(Web3(Web3.HTTPProvider(alchemy)), abi, addresses[collection])
    for i in range(max_id):
        filename = collection +'/cat'+ '/' + str(i) + '.jpg'
        if exists(filename):
            continue
        uri = mycontract.functions.tokenURI(i).call()
        r = requests.get(uri, stream = True)
        uri = r.json()['image']
        r = requests.get(uri, stream = True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')

