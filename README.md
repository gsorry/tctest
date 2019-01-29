# tctest

Simple REST API based social network in Django.
Implements User registration, JWT authentication, Posts and Likes.

## Setup and run application

1. Open /tcapp/settings.py Add `HUNTER_API_KEY` and `CLEARBIT_API_KEY` keys.
2. Run migrations:
   ```
   python manage.py migrate
   ```
3. Start application
   ```
   python manage.py runserver
   ```

## API

### Users

#### Signup user

POST users/signup
`http://127.0.0.1:8000/social_network/users/signup/`

BODY
email: test@test.com
password: test

Example Request:
```
curl --location --request POST "http://127.0.0.1:8000/social_network/users/signup/" \
  --form "email=test@test.com" \
  --form "password=test"
```

#### Login user

POST token
`http://127.0.0.1:8000/social_network/token/`

BODY
email: test@test.com
password: test

Example Request:
```
curl --location --request POST "http://127.0.0.1:8000/social_network/token/" \
  --form "email=test@test.com" \
  --form "password=test"
```

### Posts

#### List posts

GET posts
`http://127.0.0.1:8000/social_network/posts/`

Example Request:
```
curl --location --request GET "http://127.0.0.1:8000/social_network/posts/"
```

#### Create post

POST posts
`http://127.0.0.1:8000/social_network/posts/`

Example Request:
```
curl --location --request POST "http://127.0.0.1:8000/social_network/posts/" \
  --data "content=Lorem ipsum..."
```

#### Get post

GET posts/1
`http://127.0.0.1:8000/social_network/posts/1`

Example Request:
```
curl --location --request GET "http://127.0.0.1:8000/social_network/posts/1"
```

#### Like post

GET posts/1/like 
`http://127.0.0.1:8000/social_network/posts/1/like`

Example Request:
```
curl --location --request GET "http://127.0.0.1:8000/social_network/posts/1/like"
```

#### Unlike post

GET posts/1/unlike 
`http://127.0.0.1:8000/social_network/posts/1/unlike`

Example Request:
```
curl --location --request GET "http://127.0.0.1:8000/social_network/posts/1/unlike"
```
