from flask import Flask, jsonify, request
from main import extract_news

app = Flask(__name__)

@app.route('/api/news', methods=['POST'])
def get_news():
    company_name = request.json['company_name']
    articles = extract_news(company_name)
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
