import csv
all_articles = []
with open("Articles.csv",encoding="utf-8")as f:
    reader = csv.reader(f)
    data  = list(reader)
    all_articles = data[1:]

liked_articles = []
non_liked_articles = []
