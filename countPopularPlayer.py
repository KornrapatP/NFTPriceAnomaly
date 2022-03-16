import csv
from collections import Counter

collections = ['COOLS', 'PPG', 'IRENEDAO', 'BAYC']
frequency = {}
for c in collections:
    with open(c + 'tokensPaidETH.csv', 'r') as inputFile:
        inputReader = csv.reader(inputFile)
        for row in inputReader:
            frequency[row[0]] = frequency.get(row[0], 0) + 1
            frequency[row[1]] = frequency.get(row[1], 0) + 1
a = dict(Counter(frequency).most_common(30))
print(a)