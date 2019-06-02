'''

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "9MI4khhG7wBQuvoK0pPVuX6il"
consumer_secret = "oa70QGiLj8buNQpXwc9LHBRxyXCrKLSA9FvUS7V3NOpJDhetvn"
access_token = "2216994281-vNyLbe8tctUrlxirgmuZqhPrBCe5ANIFi5AecKW"
access_token_secret = "JS79GyGOVWRFAca6l2iDEc5vYwePziDmIhxa03pvnxdB4"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
'''