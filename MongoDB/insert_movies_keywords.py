import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//movies_and_keywords.csv', 'r')
reader = csv.DictReader(csvfile)

client = MongoClient('localhost', 27017)
db = client.IMDB

db.movies_and_keywords.drop()

header = [ "idkeywords", "keyword", "idmovies_keywords", "idmovies", "idkeywords", "idseries"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    #db.movies_and_keywords.insert(row)
    db.movies_with_genres.insert(row)