from flask import Flask, jsonify, request
import csv
import pandas as pd
from demographic_filtering import output
from contantBasedFiltering import get_recommondation
from storage import all_articles,liked_articles,non_liked_articles







app = Flask(__name__)

@app.route("/get-article")
def get_article():
    articles_data = {
        "title": all_articles[0][12],
        "url":all_articles[0][11],
        "text":all_articles[0][13],
        "lang":all_articles[0][14],
        "total_events":all_articles[0][15]
            }
    return jsonify({
        "data": articles_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/disliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    non_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201
    
@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "title": article[1],
            "url": article[0],
            "text": article[2] or "N/A",
            "lang": article[3],
            "total_events": article[4],
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommondation(liked_article[12])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[1],
            "url": recommended[0],
            "text": recommended[2] or "N/A",
            "lang": recommended[3],
            "total_events": recommended[4],
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if(__name__ == "__main__" ):
    app.run(debug = True,host = "localhost")
