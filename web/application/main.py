from flask import (
    Flask,
    render_template,
    request,
)

from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://db')
db = client['db']
jokes = db.jokes


@app.route('/')
def hello():
    return render_template(
        'main.html'
    )


def search_joke(keywords):
    return list(jokes.find({"$text": {"$search": keywords}}))


@app.route('/get_joke', methods=['GET'])
def get_joke():
    joke_keywords = request.args.get('keywords')
    found_jokes = search_joke(joke_keywords)
    return render_template(
        'main.html',
        jokes=found_jokes[0:-1],
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
