from faker import Faker

import click
import sys
import yaml
import urllib.request
import random
import json


class Bot:
    """
    Bot class

    """

    def __init__(self, settings_file):
        """
        Bot constructor

        :param settings_file: Settings file

        """
        with open(settings_file, 'r') as stream:
            try:
                self.settings = yaml.load(stream)
            except yaml.YAMLError as exc:
                sys.exit('Failed to load settings!')

        self.fake = Faker()

    def signup_user(self):
        """
        Signup user

        :return: User

        """
        email = bytearray(self.fake.email(), 'utf-8')
        password = bytearray('test123', 'utf-8')
        user_data = b'email=%s&password=%s' % (email, password)
        request = urllib.request.Request(url='{}users/signup/'.format(self.settings['base_url']),
                                         data=user_data,
                                         method='POST')
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    def login_user(self, user):
        """
        Login user with email and password

        :param user: User
        :return: Auth token

        """
        email = bytearray(user['email'], 'utf-8')
        password = bytearray('test123', 'utf-8')
        user_data = b'email=%s&password=%s' % (email, password)

        request = urllib.request.Request(url='{}token/'.format(self.settings['base_url']),
                                         data=user_data,
                                         method='POST')

        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    def create_post(self, token):
        """
        Create Post

        :param token: Auth token
        :return: Post

        """
        content = bytearray(self.fake.text(), 'utf-8')
        post_data = b'content=%s' % content
        headers = {'Authorization': 'Bearer {}'.format(token)}

        request = urllib.request.Request(url='{}posts/'.format(self.settings['base_url']),
                                         data=post_data,
                                         method='POST',
                                         headers=headers)

        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    def get_posts(self, page, token):
        """
        Get posts page

        :param page: Page number
        :param token: Auth token
        :return: Posts

        """
        total_posts = []
        headers = {'Authorization': 'Bearer {}'.format(token)}

        request = urllib.request.Request(url='{}posts/?page={}'.format(self.settings['base_url'], page),
                                         method='GET',
                                         headers=headers)

        response = urllib.request.urlopen(request)
        response_dict = json.loads(response.read())

        total_posts += response_dict['results']

        if response_dict['next'] is not None:
            total_posts += self.get_posts(page+1, token)

        return total_posts

    def like_post(self, post, token):
        """
        Like post

        :param post: Post
        :param token: Auth token
        :return: Like

        """
        headers = {'Authorization': 'Bearer {}'.format(token)}

        request = urllib.request.Request(url='{}posts/{}/like'.format(self.settings['base_url'], post['id']),
                                         method='GET',
                                         headers=headers)

        response = urllib.request.urlopen(request)
        return json.loads(response.read())


@click.command()
@click.option('-s', '--settings', 'settings_file', default='bot_settings.yaml', help='Bot settings file.')
def run_bot(settings_file):

    bot = Bot(settings_file)

    print('Init Bot')

    users = []

    # Create users and posts:
    for u in range(bot.settings['number_of_users']):

        new_user = bot.signup_user()

        print('Signup user {}'.format(new_user['email']))

        user_token = bot.login_user(new_user)

        print('Login user')

        posts_per_user = random.randint(1, bot.settings['max_posts_per_user'])

        for p in range(posts_per_user):
            bot.create_post(user_token['access'])

        print('Create {} posts'.format(posts_per_user))

        new_user['posts_per_user'] = posts_per_user
        users.append(new_user)

    # Sort users by posts_per_user
    sorted_users = sorted(users, key=lambda k: k['posts_per_user'], reverse=True)

    print('Sort users')

    # Like posts:
    for new_user in sorted_users:

        user_token = bot.login_user(new_user)

        print('Login user {}'.format(new_user['email']))

        all_posts = bot.get_posts(1, user_token['access'])

        print('Read all posts')

        can_like = False
        other_posts = []

        for current_post in all_posts:
            if current_post['user'] != new_user['id']:
                other_posts.append(current_post)
                if len(current_post['likes']) == 0:
                    can_like = True

        if bot.settings['max_likes_per_user'] <= len(other_posts):
            other_posts = random.sample(other_posts, bot.settings['max_likes_per_user'])

        if can_like:
            for current_post in other_posts:
                bot.like_post(current_post, user_token['access'])

            print('Like {} posts'.format(len(other_posts)))
        else:
            print('Nothing to like')


if __name__ == '__main__':
    run_bot()
