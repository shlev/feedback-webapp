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

flask - web framework
psycopg2 - database adapter to connect postgres
flask-sqlalchemy -manage postgress commands.
gunicorn.
