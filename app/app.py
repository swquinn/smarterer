import os
import json
from flask import Flask, request, make_response, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/smarterer'
db = SQLAlchemy(app)

#@app.before_request
#def before_request():

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():
    """Returns a list of all questions known to the application.
    """
    # TODO: Filtering, sorting, and pagination.
    return json_response({ 'test': 'foo' })

@app.route('/questions/create', methods=['POST'])
def create_question():
    """Creates and returns the question that adheres to the content
    of the request. If there is an error, an error response will be
    returned instead.
    """
    return json_response({ 'test': 'foo' })

@app.route('/question/<int:question_id>', methods=['GET', 'PUT'])
def question(question_id):
    """Handles requests to a specific question, identified by that
    questions ID, which is passed in as a parameter to the call.

    Keyword arguments:
    question_id -- the identifier of the question being interacted with
    """
    #if request.method == 'PUT':
    #    update_question()
    #else:
    #    show_question(question_id)

def json_response(content, status=200, headers=[]):
    """Returns a JSON response inclusive of the content and status.

    Keyword arguments:
    content -- the content to be rendered in the JSON response
    status -- optional. The status code to return (default 200)
    headers -- optional. Additional headers to include in the response
    """
    data = json.dumps(content)
    response = make_response(data, status)
    response.headers['Content-Type'] = 'application/json'
    return response

from app.entity.question import Question

# Note: apparently this needs to be below the definition of the routes--this actuall makes a lot of sense..
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
