import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

#Twitter Login Credentials
auth = tweepy.OAuthHandler('XAjruRZe6O6gen4zGLJL5VTbw', 'vw3a8tb1AnMXEEUI3HXt7Xq5CpvjB0LNEtmAf5PmJCZYkQ3RPq')
auth.set_access_token('906982976344481794-7Nbvj6fCqkcTHNVoaepvq6iIMIJxc8G', 'sDFWRJDAcscgFkGf0Sp1M4iPB0K5FLMwW6ck2y3ANMy9a')

#Watson Login Credentials
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username= "3ca320cb-0473-4ae1-9d63-a72d139c27c2",
  password= "tLrq6dXUA1D5",
  version='2017-02-27')

def nluRun(txt):
    response = natural_language_understanding.analyze(
      text= txt,
      features=Features(
        entities=EntitiesOptions(
          emotion=True,
          sentiment=True,
          limit=3),
        keywords=KeywordsOptions(
          emotion=True,
          sentiment=True,
          limit=3)))
    print(json.dumps(response, indent=2))
    return(response)

tweet = "I'm like hey what's up hello"
nluRun(tweet)
