#Simple program that demonstrates how to invoke Azure ML Text Analytics API (https://datamarket.azure.com/dataset/amla/text-analytics).
# It needs two arguments -
#   1. Account key (from https://datamarket.azure.com/account/keys)
#   2. input text string (English only)

import urllib2
import urllib

import sys
import base64
import json 

account_key = "mOMo7A5NdYf7T43ThZBaKQGUs9Y+V8kkEulZCwjR8Lo"
input_text = "test for ml"

base_url = 'https://api.datamarket.azure.com/data.ashx/amla/text-analytics/v1'
creds = base64.b64encode('AccountKey:' + account_key)
headers = {'Content-Type':'application/json', 'Authorization':('Basic '+ creds)}
params = { 'Text': input_text}

# sentiment
sentiment_url = base_url + '/GetSentiment?' + urllib.urlencode(params)
req = urllib2.Request(sentiment_url, None, headers) 
response = urllib2.urlopen(req)
result = response.read()
obj = json.loads(result)
print('Sentiment score: ' + str(obj['Score']))

# key phrases
key_phrases_url = base_url + '/GetKeyPhrases?' + urllib.urlencode(params)
req = urllib2.Request(key_phrases_url, None, headers) 
response = urllib2.urlopen(req)
result = response.read()
obj = json.loads(result)
print('Key phrases: ' + ','.join(obj['KeyPhrases']))