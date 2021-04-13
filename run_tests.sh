#!/bin/bash

cd polaroid
if [ -f ./db.sqlite3 ]; then
    echo "Previous cache of db.sqlite3 found, deleting..."
    rm -rf ./db.sqlite3
fi

python3 manage.py migrate --run-syncdb
python3 manage.py test