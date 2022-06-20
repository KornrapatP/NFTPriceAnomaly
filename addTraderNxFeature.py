import networkx as nx
import csv

# for k in ['COOLS']:
#     DG = nx.DiGraph()
#     pageranks = {}
#     i = 0
#     with open(k+'tokensProcessed.csv', 'r') as inputFile:
#         inputReader = csv.reader(inputFile)
#         with open(k+'tokensProcessedNx.csv', 'w') as outputFile:
#             outputWriter = csv.writer(outputFile)
#             outputWriter.writerow(['from', 'to', 'tokenId', 'blockNumber', 'transactionIndex', 'transactionHash', 'ETH', 'isOpensea', 'isSenderContract', 'isRecceiverContract', 'pSale', 'median1000', 'bPR', 'sPR', 'bDG', 'sDG'])
#             for row in inputReader:
#                 i+=1
#                 print(i)
#                 if row[0] == 'from':
#                     continue
#                 deg = dict(DG.degree)
#                 outputWriter.writerow(row+[pageranks.get(row[1],0), pageranks.get(row[0],0), deg.get(row[1],0), deg.get(row[0],0)])
#                 DG.add_weighted_edges_from([(row[0], row[1], float(row[6]))])
#                 pageranks = nx.pagerank(DG)


for k in ['COOLS']:
    DG = nx.DiGraph()
    pageranks = {}
    i = 0
    with open(k+'tokensProcessed.csv', 'r') as inputFile:
        inputReader = csv.reader(inputFile)
        for row in inputReader:
            if row[0] == 'from':
                    continue
            DG.add_weighted_edges_from([(row[0], row[1], float(row[6]))])
    pageranks = nx.pagerank(DG)
    deg = dict(DG.degree)

    with open(k+'tokensProcessed.csv', 'r') as inputFile:
        inputReader = csv.reader(inputFile)
        with open(k+'tokensProcessedNx2.csv', 'w') as outputFile:
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(['from', 'to', 'tokenId', 'blockNumber', 'transactionIndex', 'transactionHash', 'ETH', 'isOpensea', 'isSenderContract', 'isRecceiverContract', 'pSale', 'median1000', 'bPR', 'sPR', 'bDG', 'sDG'])
            for row in inputReader:
                i+=1
                print(i)
                if row[0] == 'from':
                    continue
                outputWriter.writerow(row+[pageranks.get(row[1],0), pageranks.get(row[0],0), deg.get(row[1],0), deg.get(row[0],0)])
                