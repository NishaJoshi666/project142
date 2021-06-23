import csv

all_articles = []
with open('articles.csv',errors = 'ignore') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_likes_articles = []
did_not_read_articles = []