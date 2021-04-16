#!/bin/bash

cd polaroid
if [ -f ./db.sqlite3 ]; then
    echo "Previous cache of db.sqlite3 found, deleting..."
    rm -rf ./db.sqlite3
fi

python3 manage.py migrate --run-syncdb
echo "from api_auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell