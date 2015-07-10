#!/bin/bash
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

IP_ADDRESS="$(ifconfig | grep '\<inet\>' | sed -n '1p' | tr -s ' ' | cut -d ' ' -f3 | cut -d ':' -f2)"

echo -e "[INFO ] Installing python tools and dependencies..."
sudo apt-get update
sudo apt-get install -y python2.7 python2.7-dev python-pip

echo -e "[INFO ] Installing Flask..."
pip install Flask

echo -e "[INFO ] Installing SQLAlchemy..."
pip install sqlalchemy

echo -e "[INFO ] Installing Flask-SQLAlchemy..."
pip install Flask-SQLAlchemy

echo -e "[INFO ] Installing postgres and resetting password for: 'postgres' to: 'postgres'..."
sudo apt-get install -y postgresql postgresql-contrib postgresql-server-dev-all
sudo -u postgres psql --command "ALTER USER postgres WITH PASSWORD 'postgres';"
sudo -u postgres psql --command "CREATE EXTENSION adminpack;"

echo -e "[INFO ] Creating database: 'smarterer'..."
sudo -u postgres createdb smarterer

echo -e "[INFO ] Configuring postgres for host accessibility..."
sudo sed -i "s/^#listen_addresses\s=\s.*$/listen_addresses = '*'/" /etc/postgresql/9.4/main/postgresql.conf
sudo sh -c "echo 'host all all $IP_ADDRESS/24 trust' >> /etc/postgresql/9.4/main/pg_hba.conf"

echo -e "[INFO ] Restarting postgres service..."
sudo service postgresql restart

echo -e "[INFO ] Installing psycopg2..."
pip install psycopg2
