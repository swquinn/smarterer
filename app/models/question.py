# Copyright (c) 2015 Sean Quinn
#
# Licensed under the MIT License (http://opensource.org/licenses/MIT)
#
# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from sets import Set
from app import db

class Question(db.Model, ):

    __tablename__ = 'questions'

    """The object ID of the question."""
    id = db.Column(db.Integer, primary_key=True)

    """The question's text."""
    text = db.Column(db.String)

    """The correct answer to the question."""
    answer = db.Column(db.String)

    """The list of choices presented to the user, choices do not
    necessarily include the answer as well as distractors but
    depending on user data, they could.
    """
    choices = db.Column(db.String)

    def __init__(self, text, answer, choices):
        self.text = text
        self.answer = answer
        self.choices = choices

    def __repr__(self):
        return "<Question(text='%s', answer='%s', choices='%s')>" % (self.text, self.answer, self.choices)

    def delete(self):
        """Deletes this question.
        """
        # TODO

    def to_dict(self):
        """Returns the question as a dictionary to allow for JSON
        serialization of the question's data (otherwise, the server
        complains... loudly).
        """
        #[field.name: getattr(self, field.name) for field in self.__table__.columns }]
        return {
            'id': self.id,
            'text': self.text,
            'answer': self.answer,
            'choices': [item.strip() for item in self.choices.split(',')]
        }

    def update(self, data):
        """Updates this question with passed data.
        """
        # TODO

    def get_all_choices(self):
        """Returns an unordered set of all the possible answer choices
        for a question, this includes the correct answer as well.
        """
        items = Set([item.strip() for item in self.choices.split(',')])
        items.add(self.answer)
        return items
