#!/bin/bash
# Called by start-dev.sh and start-docker.sh, which sets
#    - DATABASE_HOST
#    - DJANGO_SUPERUSER
#    - DJANGO_SUPERUSER_PASSWORD
#    - DJANGO_SUPERUSER_EMAIL
echo Admin user = $DJANGO_SUPERUSER email = $DJANGO_SUPERUSER_EMAIL
if [[ $1 != "" ]]; then
    port=$1
elif [[ $DJANGO_PORT != "" ]]; then
    port=$DJANGO_PORT
else
    port=8000
fi
echo Port is $port
echo DJANGO_SETTINGS_MODULE $DJANGO_SETTINGS_MODULE

echo .
echo --- Executing python manage.py makemigrations ---
echo .
python manage.py makemigrations django_kb_app
makemigration_success=$?

echo .
echo --- Executing python manage.py migrate ---
echo .
python manage.py migrate
migrate_success=$?

echo .
echo --- Executing python manage.py populatedata ---
echo .
python manage.py populatedata
populatedata_success=$?

echo Executing python manage.py shell to check if user exists
python manage.py shell -c "from django_kb_app.models import User; print(User.objects.filter(username='$DJANGO_ADMIN').exists())"
superuser_exists=$?

echo .
echo .
echo .
if [ $superuser_exists -eq 1 ]; then
  echo .
  echo --- Executing python manage.py createsuperuser ---
  echo .
  python manage.py createsuperuser --username $DJANGO_SUPERUSER --email $DJANGO_SUPERUSER_EMAIL --no-input
else
  echo --- INFO: Skipping python manage.py createsuperuser - super user $DJANGO_SUPERUSER already exists.
fi
createsuperuser_success=$?

success=0
if [ $makemigration_success -eq 1 ]; then
  success=1
  echo --- ERROR: python manage.py makemigrations failed.  See errors above.
fi

if [ $migrate_success -eq 1 ]; then
  success=1
  echo --- ERROR: python manage.py migrate failed.  See errors above.
fi

if [ $populatedata_success -eq 1 ]; then
  success=1
  echo --- ERROR: python manage.py populatedata failed.  See errors above.
fi

if [ $createsuperuser_success -eq 1 ]; then
  success=1
  echo --- ERROR: python manage.py createsuper failed.  See errors above.
fi

if [ $success -eq 1 ]; then
  read -p "Press [Ctrl-c] to abort, [Enter] to run server with errors..."
fi

python manage.py runserver 0.0.0.0:$port
