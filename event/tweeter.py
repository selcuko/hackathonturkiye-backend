import tweepy
import json
import os


if os.path.exists('twitter_auth.json'):
    secrets = json.load(open('twitter_auth.json'))

    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

    twitter = tweepy.API(auth)


def tweet_event(event):

    try:
        status = twitter.update_with_media(event.thumbnail.path, 
        f'Yeni {event.etype.name}: {event.title}\n{event.url}')
        return True, status

    except Exception as exc:
        if not os.path.exists('twitter_auth.json'): 
            return False, Exception('twitter_auth.json dosyası yok.')
        return False, exc