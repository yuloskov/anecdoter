import csv
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['db']
jokes = db.jokes
jokes_csv_path = '/home/yuloskov/Innopolis/BS_3/Fall/DSs/project1/shortjokes.csv'

with open(jokes_csv_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        j = ''.join([r + ',' for r in row[1:]])
        jokes.insert_one({'joke': j[1:-2]})

# js = list(jokes.find({}))
# for j in js:
#     print(j)

jokes.create_index([('joke', 'text')])
