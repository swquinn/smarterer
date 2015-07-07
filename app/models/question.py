from app import db

class Question(db.Model):

    __tablename__ = 'questions'

    """The object ID of the question."""
    id = db.Column(db.Integer, primary_key=True)

    """The question's text."""
    text = db.Column(db.String)

    """The correct answer to the question."""
    answer = db.Column(db.String)

    """The list of choices presented to the user, choices include the
    answer, as well as the distractors.
    """
    choices = db.Column(db.String)

    def __init__(self, text, answer, choices):
        self.text = text
        self.answer = answer
        self.choices = choices

    def __repr__(self):
        return "<Question(text'%s', answer='%s', choices='%s')>" % (self.text, self.answer, self.choices)

    def delete(self):
        """Deletes this question.
        """
        # TODO

    def update(self, data):
        """Updates this question with passed data.
        """
        # TODO
