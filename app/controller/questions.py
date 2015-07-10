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
from flask import request

@app.route('/questions')
def list_questions():
    """Returns a list of all questions known to the application.
    """
    # TODO: Sorting
    query = Question.query
    questions = []
    limit = -1

    ## Get the limit from the query parameters, this will
    ## be used both for paginated and non-paginated queries
    if 'limit' in request.args:
        limit = int(request.args['limit'])

    ## If the user has specified a "page" then we're going
    ## to assume that they want their results to be paginated.
    ##
    ## This is a good first pass, but what if the user specifies
    ## a page that is out of range? They get a 404... this
    ## might be OK. Need to think on it a bit more. [SWQ]
    if 'page' in request.args:
        limit = limit if limit > 0 else 10
        questions = query.paginate(int(request.args['page']), limit).items
    else:
        if limit > 0:
            query.limit(limit)
        questions = query.all

    results = [q.to_dict() for q in questions]
    return json_response({ 'results': results })

@app.route('/questions/create', methods=['POST'])
def create_question():
    """Creates and returns the question that adheres to the content
    of the request. If there is an error, an error response will be
    returned instead.
    """
    data = request.data
    if not ('text' in data):
        raise Exception('Error: Question text is required.')
    if not ('answer' in data):
        raise Exception('Error: Question answer is required.')
    if not ('choices' in data):
        raise Exception('Error: Question answer choices are required.')

    #validate question? yeesh... let's keep it simple for now...
    question = Question(text=data.text, answer=data.answer, choices=data.choices)
    db.session.add(question)
    db.session.commit()
    return json_response(question, 201)
