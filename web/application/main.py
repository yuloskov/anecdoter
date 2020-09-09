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
        'main.html',
        no_searches=True,
    )


def search_joke(keywords, page):
    page_size = 10
    offset = page * page_size
    res = list(jokes.find({"$text": {"$search": keywords}}).skip(offset).limit(page_size + 1))
    return res[:-1], len(res) > page_size


@app.route('/get_joke', methods=['GET'])
def get_joke():
    joke_keywords = request.args.get('keywords')
    page = int(request.args.get('page', 0))
    found_jokes, next_page = search_joke(joke_keywords, page)
    return render_template(
        'main.html',
        keywords=joke_keywords,
        jokes=found_jokes,
        no_searches=False,
        page=page,
        next_page=next_page
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
