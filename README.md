1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py loaddata paste/fixtures/initial_data.json
4. Install rabbitmq
5. Start celery -- python manage.py celeryd --loglevel INFO  -E -B -c 1 &
6. python manage.py runserver



### Example Site ###

[ypaste.yakupadakli.com](http://ypaste.yakupadakli.com/)
