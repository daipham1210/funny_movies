## Funny Movies

A web application that allows users to share youtube videos

Live demo: https://funny-movies-remi.herokuapp.com/
## Installation
- Install python 3, pip
- create & activate virtuanl env 
```
python3 -m venv .venv
source .venv/bin/activate
``` 
- create .env from .env.sample
- Instail libruary:
```
pip install -r requirements.txt
```
- Start server
```
python manage.py migrate
python manage.py runserver
```

## Test
- Example Integration Test: https://github.com/daipham1210/funny_movies/blob/master/user/tests.py#L14
- Example Unit Test: https://github.com/daipham1210/funny_movies/blob/master/movies/tests.py#L6
