## Funny Movies

A web application that allows users to share youtube videos

## Installation
- Install python 3, pip
- create & activate virtuanl env 
```
python3 -m venv .venv
source .venv/bin/activate
``` 
- Generate SECRET_KEY
```
echo "SECRET_KEY=$(openssl rand -base64 32)" > .env
```
- Instail libruary:
```
pip install -r requirements.txt
```
- Start server
```
python manage.py migrate
python manage.py runserver
```