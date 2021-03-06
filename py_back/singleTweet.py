#This script analyzes the NL of a single tweet form a single user using WATSON AI NLU API

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

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
    return response
