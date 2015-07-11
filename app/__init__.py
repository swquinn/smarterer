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
import os
import json
from flask import Flask, jsonify, request, make_response, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost/smarterer'
# TODO: Getting errors about Flask having "no attribute 'json'"
#app.json_encoder = app.json.encoder.JSONEncoder
db = SQLAlchemy(app)

err_messages = {
    404: 'We couldn\'t find that resource you were looking for.',
    405: 'The method you\'ve requested this resource with is not supported.',
    500: 'Oops! It looks like something went very, very wrong.'
}
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def error_page(error):
    resp = {
        'code': error.code,
        'message': error.name,
        'description': err_messages[error.code]
    }
    return json_response(resp, error.code)

def json_response(content, status=200, headers={}):
    """Returns a JSON response inclusive of the content and status.

    Keyword arguments:
    content -- the content to be rendered in the JSON response
    status -- optional. The status code to return (default 200)
    headers -- optional. Additional headers to include in the response
    """
    #data = json.dumps(content)
    #response = make_response(data, status)
    response = jsonify(content)
    response.status_code = status
    return response

from app.models.question import Question
from app.controller import index, question, questions
