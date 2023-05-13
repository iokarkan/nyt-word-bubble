from flask import current_app
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nyt_word_bubble import db
import os
import numpy as np


nltk.download("punkt")
nltk.download("stopwords")


def fetch_nytimes_articles(period=1):
    api_key = current_app.config['NYT_API_KEY']
    url = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/{period}.json?api-key={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json()["results"]
        top50 = process_articles(articles)

        return top50
    else:
        print(f"Error fetching articles: {response.status_code}")


def write_nyt_to_db(table, top50):
    with current_app.app_context():
        # flush prev table
        table.query.delete()
        db.session.commit()

        for i, word_dic in enumerate(top50):
            word = table(
                id=i + 1, word=word_dic["word"], frequency=int(word_dic["frequency"])
            )
            db.session.add(word)
            db.session.commit()


def process_articles(articles):
    all_words = []
    stop_words = set(stopwords.words("english"))

    for article in articles:
        # Extract the article content
        content = f"{article['title']}\n{article['abstract']}"

        # Tokenize the content
        words = word_tokenize(content)

        # Remove stopwords and non-alphanumeric characters
        words = [
            word.lower()
            for word in words
            if word.isalnum() and word.lower() not in stop_words
        ]

        # Add the words to the list
        all_words.extend(words)

    # Count the frequency of each word
    word_counts = np.unique(all_words, return_counts=True)

    # Sort the words based on their frequency
    sorted_indices = np.argsort(word_counts[1])[::-1]

    # Get the top 50 most frequent words and their frequencies
    top_50_words = word_counts[0][sorted_indices][:50]
    top_50_frequencies = word_counts[1][sorted_indices][:50]

    # Convert the words and frequencies to a list of dictionaries
    word_frequency_list = [
        {"word": word, "frequency": freq}
        for word, freq in zip(top_50_words, top_50_frequencies)
    ]

    return word_frequency_list