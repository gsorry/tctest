from faker import Faker

import sys
import yaml
import urllib.request
import random
import json


with open('bot_settings.yaml', 'r') as stream:
    try:
        settings = yaml.load(stream)
    except yaml.YAMLError as exc:
        sys.exit('Failed to load settings!')

fake = Faker()


def signup_user():
    """
    Signup user

    :return: User

    """
    email = bytearray(fake.email(), 'utf-8')
    password = bytearray('test123', 'utf-8')
    user_data = b'email=%s&password=%s' % (email, password)
    request = urllib.request.Request(url='{}users/signup/'.format(settings['base_url']),
                                     data=user_data,
                                     method='POST')
    response = urllib.request.urlopen(request)
    return json.loads(response.read())


def login_user(user):
    """
    Login user with email and password

    :param user: User
    :return: Auth token

    """
    email = bytearray(user['email'], 'utf-8')
    password = bytearray('test123', 'utf-8')
    user_data = b'email=%s&password=%s' % (email, password)

    request = urllib.request.Request(url='{}token/'.format(settings['base_url']),
                                     data=user_data,
                                     method='POST')

    response = urllib.request.urlopen(request)
    return json.loads(response.read())


def create_post(token):
    """
    Create Post

    :param token: Auth token
    :return: Post

    """
    content = bytearray(fake.text(), 'utf-8')
    post_data = b'content=%s' % content
    headers = {'Authorization': 'Bearer {}'.format(token)}

    request = urllib.request.Request(url='{}posts/'.format(settings['base_url']),
                                     data=post_data,
                                     method='POST',
                                     headers=headers)

    response = urllib.request.urlopen(request)
    return json.loads(response.read())


users = {}

for u in range(settings['number_of_users']):

    current_user = signup_user()
    current_token = login_user(current_user)

    for p in range(random.randint(1, settings['max_posts_per_user'])):
        create_post(current_token['access'])

    users[current_user['id']] = current_user

print(users)
