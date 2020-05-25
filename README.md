> ### Install dependencies
```
pip install -r requirements.txt
```

<br/>

> ### Run development server
```
python manage.py runserver
```

<br/>

> ### API
| Path | Function |
| --- | --- |
| localhost:8000 | API Root
| localhost:8000/admin | Admin Panel
| localhost:8000/swagger | Swagger
| localhost:8000/redoc | ReDoc

> ### Event filters
| Keyword | Example |
| --- | --- |
| location | ?location=izmir |
| after | ?after=2020-01-01 |
| before | ?before=2020-01-01 |
| etype | ?etype=ideathon |