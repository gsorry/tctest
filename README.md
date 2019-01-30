# tctest

Simple REST API based social network in Django.
Implements User registration, JWT authentication, Posts and Likes.

## Setup and run application

1. Open /tcapp/settings.py Add `HUNTER_API_KEY` and `CLEARBIT_API_KEY` keys.
2. Set python path:
   ```
   export PYTHONPATH=`pwd`
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start application
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

## Bot

### Bot config

Bot settings are stored in `bot_settings.yaml`:
```
base_url: 'http://127.0.0.1:8000/social_network/'
number_of_users: 3
max_posts_per_user: 3
max_likes_per_user: 4
```

### Run Bot

1. Set python path:
   ```
   export PYTHONPATH=`pwd`
   ```
2. Check bot options:
   ```
   python bot.py --help
   ```
2. Run bot to test API functionalities:
   ```
   python bot.py [-s bot_settings.yaml]
   ```
It will create some users (`number_of_users`) and random number of posts for each user but no more then `max_posts_per_user`.

After sorting users by number of posts, Bot sends likes for other posts no more then `max_likes_per_user`.
