import unittest
from flask import current_app, url_for
from nyt_word_bubble import create_app, db
from nyt_word_bubble.api.routes import WordFrequencyDay 

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_api_day_word(self):
        day_word = WordFrequencyDay(id=1, word="Test", frequency=2)
        db.session.add(day_word)
        db.session.commit()
        response =  self.client.get(url_for('api.word_bubble_data_day'))
        self.assertEqual(response.json, [{'frequency': 2, 'id': 1, 'word': 'Test'}])
        db.session.delete(day_word)
        db.session.commit()


