import networkx as nx
import csv
all_cycles = []
for k in ['COOLS']:
    for i in range(12743224, 14149228, 100):
        print(i)
        start = i
        end = start + 1066
        q = nx.DiGraph()
        pageranks = {}
        with open(k+'tokensProcessed.csv', 'r') as inputFile:
            inputReader = csv.reader(inputFile)
            for row in inputReader:
                if row[0] == 'from' or int(row[3])<start:
                    continue
                if int(row[3]) > end:
                    break
                q.add_weighted_edges_from([(row[0], row[1], float(row[6]))])
        # print(pageranks)
        g = nx.strongly_connected_components(q)
        counter = 0
        with open(k+'washTradeCandidates_4hours.csv', 'a') as outputFile:
            outputWriter = csv.writer(outputFile)
            for a in g:
                counter +=1
                if len(a)>15 or len(a) == 1:
                    continue
                print(counter)
                outputWriter.writerow([start, end, a])
print(all_cycles)