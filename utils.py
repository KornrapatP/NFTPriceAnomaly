from web3 import Web3

def create_contract(web3, abi, address):
    contract = web3.eth.contract(address=address, abi=abi)
    return contract
