~~~~~~~ To dev locally:
- open connection to LOCAL or CLOUD db (instructions below)
start virtual env & start server
- 'cd shareplay_backend'
- 'source env/bin/activate'
- in 'shareplay_backend'
- './manage.py runserver 0.0.0.0:8000'
some notes:
- make sure you're on the same wifi as the server
- make sure the app is pointing to the correct address

~~~~~~~ Open connection to LOCAL db:
- 'mysql.server start'
- 'mysql -uroot -p'


~~~~~~~ Open connection to CLOUD db:
start connection to sql DB:
- in 'shareplay_backlend'
- './cloud_sql_proxy -instances="shareplay-204722:us-east4:polls-instance"=tcp:3306'
to connect to db, in another tab:
- mysql --host 127.0.0.1 --user root --password

