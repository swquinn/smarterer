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
from app import app, db, json_response
from app.models.question import Question

@app.route('/question/<int:question_id>', methods=['GET'])
def get_question(question_id):
    """Returns a specific question, by its question ID, which is passed
    in as a parameter to the call.

    Keyword arguments:
    question_id -- the identifier of the question being interacted with
    """
    question = Question.query.filter_by(id=question_id).first()
    return json_response(question.to_dict())

@app.route('/question/<int:question_id>', methods=['PUT', 'PATCH'])
def update_question(question_id):
    """Handles requests to a specific question, identified by that
    questions ID, which is passed in as a parameter to the call.

    Keyword arguments:
    question_id -- the identifier of the question being interacted with
    """
    data = request.form
    question = Question.query.filter_by(id=question_id).first()
    question.update(data)
    return json_response(None, 204)
