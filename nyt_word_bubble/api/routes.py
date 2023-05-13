from flask import jsonify, current_app
from . import bp as api

from .main import fetch_nytimes_articles, write_nyt_to_db
from nyt_word_bubble.models import WordFrequencyDay, WordFrequencyWeek

@api.route("/word_bubble_data_week")
def word_bubble_data_week():
    words = WordFrequencyWeek.query.all()

    if len(words) == 0:
        top50 = fetch_nytimes_articles(period=7)
        write_nyt_to_db(WordFrequencyWeek, top50)

    words = [
        {"id": i.id, "word": i.word, "frequency": i.frequency}
        for i in WordFrequencyWeek.query.all()
    ]

    return jsonify(words)


@api.route("/word_bubble_data_day")
def word_bubble_data_day():
    words = WordFrequencyDay.query.all()

    if len(words) == 0:
        top50 = fetch_nytimes_articles(period=1)
        write_nyt_to_db(WordFrequencyDay, top50)

    words = [
        {"id": i.id, "word": i.word, "frequency": i.frequency}
        for i in WordFrequencyDay.query.all()
    ]

    return jsonify(words)