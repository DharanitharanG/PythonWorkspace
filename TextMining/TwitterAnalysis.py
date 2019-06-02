import tweepy

consumer_key = "xh5YgRu0rdFpD620t1Fx65OKb"
consumer_secret = "KlfTeCVTJm4PghRFKoGPqNyqNCGh2rQ88qAyVrm2z2dUFVey2F"
access_token = "1100224180283469824-i3KdP4FM699dANVUss2bHSPoA4Sh3H"
access_token_secret = "9ei3jvDMIiBGv72stHXzaaQW1eyc9nMRKe2LoD8NgTNvp"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api = tweepy.API(auth)

# The search term you want to find
query = "lokshaba"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
rahul = api.search(q='rahul', lang=language)
mamta = api.search(q='mamta',lang=language)
modi = api.search(q='modi',lang=language)

rahul_tweets = []
for tweet in rahul:
   rahul_tweets.append(tweet)
