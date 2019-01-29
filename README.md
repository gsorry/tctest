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

POST users/signup
http://127.0.0.1:8000/social_network/users/signup/
BODY
emailtest@test.com
passwordtest
Example Request
```
curl --location --request POST "http://127.0.0.1:8000/social_network/users/signup/" \
  --form "email=test@test.com" \
  --form "password=test"
```

POST token Copy
http://127.0.0.1:8000/social_network/token/
BODY
emailtest@test.com
passwordtest
Example Request
```
curl --location --request POST "http://127.0.0.1:8000/social_network/token/" \
  --form "email=test@test.com" \
  --form "password=test"
```

### Posts

GET posts 
http://127.0.0.1:8000/social_network/posts/
```
curl --location --request POST "http://127.0.0.1:8000/social_network/token/" \
  --form "email=test@test.com" \
  --form "password=test"
```

POST posts 
http://127.0.0.1:8000/social_network/posts/
```
curl --location --request POST "http://127.0.0.1:8000/social_network/posts/" \
  --data ""
```

GET posts /1 
http://127.0.0.1:8000/social_network/posts/1
```
curl --location --request GET "http://127.0.0.1:8000/social_network/posts/1" \
  --data ""
```

GET posts /1/like 
http://127.0.0.1:8000/social_network/posts/1/like
```
curl --location --request GET "http://127.0.0.1:8000/social_network/posts/1/like" \
  --data ""
```

GET posts /1/unlike 
http://127.0.0.1:8000/social_network/posts/1/unlike
```
curl --location --request GET "http://127.0.0.1:8000/social_network/posts/1/unlike" \
  --data ""
```


