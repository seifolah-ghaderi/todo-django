##Login
as `devloper`:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/auth/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFToken: 9omt50n4JcJokUAKW6JwTEQFxrw4zAjyxz0AaYO4xSKWsXMrEwAM92BXu0b1GkHE' \
  -d '{
  "username": "seifoo",
  "password": "SeifP@ssword123"
}'
```

as `Project Manager`:
	
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/auth/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFToken: 9omt50n4JcJokUAKW6JwTEQFxrw4zAjyxz0AaYO4xSKWsXMrEwAM92BXu0b1GkHE' \
  -d '{
  "username": "Moghadam",
  "password": "AliP@ssword123"
}'
```
output will be like this:
`{"expiry":"2022-10-02T22:08:46.344681Z","token":"36fa791d01d052f7ce204b0fb2e4bd15300a4889c941c016f10d3a0fec9e548d"}`

in swagger -> click autorize > type `token`+spase+`[token]`

--
## Setup
```
python3 -m venv vend
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

### Build docker
`docke build -t todo-rest .`
* Run
  `docker run --rm -d --name todo-rest mytodo`
  