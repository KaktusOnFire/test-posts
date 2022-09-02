# test-posts
Test case with Django

## Setup
```
docker-compose up --build -d
```

## Create admin account
```
docker-compose exec web python manage.py createsuperuser
```