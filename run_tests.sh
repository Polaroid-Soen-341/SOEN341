#!/bin/bash

check_and_delete () {
    if [ -d "$1" ]; then
        echo "$1 found, deleting..."
        rm -rf "$1"
    fi
}

cd polaroid

if [ -f ./db.sqlite3 ]; then
    echo "Previous cache of db.sqlite3 found, deleting..."
    rm -rf ./db.sqlite3
fi

locations=("content/__pycache__" "content/migration" "api_auth/__pycache__" "api_auth/migrations" "polaroid/__pycache__")
for l  in "${locations[@]}"
do
    check_and_delete "$l"
done

python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
python3 manage.py test