import csv

print(sum(1 for row in open('openseaDecode.csv')))

print(sum(1 for row in open('openseaTransactions.csv')))