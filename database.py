#!/usr/bin/python
#
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
import csv
from app import db
from app.models.question import Question

print '[INFO ] Dropping database schema...'
db.drop_all()

print '[INFO ] Creating database schema...'
db.create_all()

filename = './data/smarterer_code_challenge_question_dump.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f, delimiter='|', quoting=csv.QUOTE_NONE)
    try:
        for row in reader:
            q = Question(text=row[0], answer=row[1], choices=row[2])
            db.session.add(q)
    except csv.Error as err:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, err))

    db.session.commit()
