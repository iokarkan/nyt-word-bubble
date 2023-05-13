import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from nyt_word_bubble import create_app, db
from nyt_word_bubble.models import WordFrequencyDay, WordFrequencyWeek
from flask_migrate import Migrate, upgrade

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        words_week=WordFrequencyWeek,
        words_day=WordFrequencyDay,
    )


@app.cli.command()
def test():
    import unittest

    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision 
    upgrade()
    # create or update user roles
    