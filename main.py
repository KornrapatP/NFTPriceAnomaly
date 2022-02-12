import requests
import csv
import time

# with open('rawTransaction.csv', 'a') as csvfile:
#   dataWriter = csv.writer(csvfile)
#   i = 14030976
#   while (i < 14148229):
#     print(i)
#     if i==5774647:
#         0/0
#     response = requests.get("https://api.etherscan.io/api?module=account&action=txlist&address=0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b&startblock="+str(i)+"&endblock=14148229&page=1&offset=10000&sort=asc&apikey=VT61NKG9YRV42KUF78AGCW279Q4ZH757YE")
#     numWrote = 0
#     dataWriter.writerow(['blockNumber', 'timeStamp', 'hash', 'nonce', 'blockhash', 'txnIndex', 'from', 'to', 'value', 'gas', 'gasPrice', 'isError', 'txreceipt_status', 'input', 'contractAddress', 'cumulativeGasUsed', 'gasUsed', 'confirmations'])
#     for obj in response.json()['result']:
#       dataWriter.writerow(obj.values())
#       numWrote += 1
#       if numWrote == 10000:
#           i = int(obj['blockNumber'])
#           print(i)
#           break

# file = open("rawTransaction.csv")
#
# reader = csv.reader(file)
# #
# skip = True
# # # *_, last = reader
# # # print(last)
# # # 0/0
# i=0
# for row in reader:
#     if skip:
#         skip = False
#         continue
#     print(row[11])
#     i+=1
#     if i==20:
#         break
# file.close()


ind = 0
with open('openseaTransactions.csv', 'r') as inputFile:
    inputReader = csv.reader(inputFile)
    seen1 = set([])
    with open('openseaTransactions2.csv', 'w') as outputFile:
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(['blockNumber', 'timeStamp', 'hash', 'nonce', 'blockhash', 'txnIndex', 'from', 'to', 'value', 'gas', 'gasPrice', 'isError', 'txreceipt_status', 'input', 'contractAddress', 'cumulativeGasUsed', 'gasUsed', 'confirmations'])
        for row in inputReader:
            ind=ind+1
            if (ind%10000==0):
                print(ind)
            if (row[0] == 'blockNumber'):
                continue
            elif (row[2] not in seen1):
                seen1.add(row[2])
                outputWriter.writerow(row)


# ind = 0
# with open('openseaTransactions.csv', 'r') as inputFile:
#     inputReader = csv.reader(inputFile)
#     seen1 = set([])
#     for row in inputReader:
#         if row[0]=='13103524':
#             print(row[0], row[2], row[5])
