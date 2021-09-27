# feedback-webapp

## pipenv

same as npm

| command                             | whatis                          | comments          |
| ----------------------------------- | ------------------------------- | ----------------- |
| pip install pipenv                  | install pipenv                  | must have python3 |
| pipenv shell                        | activate enviroment             |                   |
| exit                                | exit enviroment                 |                   |
| pipenv install                      | install packges                 |                   |
| pipenv uninstall                    | uninstall                       |                   |
| pipenv lock -r                      | list env packages               |                   |
| pipenv install -r <requirments.txt> | install requirments file        | list of packages  |
| pipenv install --ignore-pipfile     | install dev version of packeges |                   |

### python packages

- flask - web framework
- psycopg2 - database adapter to connect postgres
- flask-sqlalchemy -manage postgress commands.
- gunicorn - http lib

<br><br>

- api
  - default page
  - post request
- postgres alchemy
  - create table
  - write data
- smtp
  - send mail

### Heroku

- heroku login
- heroku create <app-name>
- heroku addons:create heroku-postgresql:hobby-dev --app <app-name> => create db for app
- heroku config --app <app-name> => get app config
- Procfile => define run file. (using gunicorn)
- runtime.txt => python-version
- pip freeze > requirements.txt => save python libs

### python

- pip freeze > requirements

# Links

[mailtrap.io](mailtrp) - email sandbox service
[https://devcenter.heroku.com/articles/python-runtimes](python heroku)

<br><br>

# issues

not compiled - [venv setting](https://techinscribed.com/python-virtual-environment-in-vscode/)
