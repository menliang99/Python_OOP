import oauth2
import urllib.parse as urlparse


class TwitterConsoleLogin:
    def __init__(self, consumer_key, consumer_secret):
        # create a consumer, which uses CONSUMER_KEY and CONSUMER_SECRET to identify our app uniquely.
        self.__consumer = oauth2.Consumer(consumer_key, consumer_secret)

    def perform_twitter_login(self):   #encapsulate the code by making method to be private "__" before the method.
        request_token = self.__get_request_token()
        verifier = self.__get_oauth_verifier(request_token)
        return self.__get_access_token(request_token, verifier)


    def __get_request_token(self):
        client = oauth2.Client(self.__consumer)
        # use client to perform a request for the request token
        response, content = client.request('https://api.twitter.com/oauth/request_token', 'POST')
        if response.status != 200:
            print("An error occured getting the the request token from twitter.")

        # Get the request token parsing the query string returned.
        return dict(urlparse.parse_qsl(content.decode('utf-8')))

    def __get_oauth_verifier(self, request_token):
        # Ask user to authorize our app and give us the pin code
        print("Go to the following site in your brower: ")
        print(self.__get_oauth_verifier_url(request_token))
        return input("What is the PIN? ")

    def __get_oauth_verifier_url(self, request_token):
        return "{}?oauth_token={}".format('https://api.twitter.com/oauth/authorize', request_token['oauth_token'])

    def __get_access_token(self, request_token, oauth_verifier):
        # Create a token object which contains the request token, and the verifier.
        token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
        token.set_verifier(oauth_verifier)

        # Create a client with our consumer and the newly created token
        client = oauth2.Client(self.__consumer, token)

        # Ask twitter for an access token, and Twitter knows it should give us it because we have verified the request
        # token.
        response, content = client.request('https://api.twitter.com/oauth/access_token', 'POST')
        return dict(urlparse.parse_qsl(content.decode('utf-8')))


twitter_login = TwitterConsoleLogin('my_key', 'my_secret')
twitter_login.perform_twitter_login()

