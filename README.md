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
- .bash_profile

### Heroku

- heroku login
- heroku create <app-name>
- heroku addons:create heroku-postgresql:hobby-dev --app <app-name> => create db for app
- heroku config --app <app-name> => get app config
- Procfile => define run file. (using gunicorn)
- runtime.txt => python-version
- pip freeze > requirements.txt => save python libs
- link heroku to git
  heroku git:remote -a <git-repository>
- git push heroku main => update branch to heroku
- heroku open
- heroku run python

### python

- pip freeze > requirements

# Links

[mailtrp](mailtrap.io) - email sandbox service <br>
[python heroku](https://devcenter.heroku.com/articles/python-runtimes)<br>
[deploy python on heroku](https://gist.github.com/bradtraversy/0029d655269c8a972df726ed0ac56b88)
<br><br>

# issues

not compiled - [venv setting](https://techinscribed.com/python-virtual-environment-in-vscode/)
