#!/usr/bin/python2.7 -tt

#Import the necessary methods from tweepy library
import json
import re
from twilio.rest import TwilioRestClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = 'rvyCmF9B8X348O0yzLCMADEHQ'
consumer_secret = 'NJeTfA6vIny7c2y4b9Jl38cPSQGbLhGCwAhXNt1fGCHscHAcrp'
access_token = '193453505-7jVDGjIoTKcbHytGAB73nJZugdVuzFIgzJEiYI1M'
access_token_secret = 'oDy27ogsMOnZG5VlYHqHteoTpSXAMotXQ7NiajbQ2bvCx'
accountSID = 'AC3fa8ad7abc08e1e1ea9e65968c350455'
authToken = '02c503b5510dfae9ad98ad9480b3df27'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+12108803073'
myCellPhone = '+12105088159'
keywords = ['nmd', 'ultra boost']

def find_words(str):
    for word in keywords:
        match = re.search(word, str, re.IGNORECASE)
        if match:
            print 'Found ', match.group()
            return True
    return False

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print "New Tweet!"
        print data
        data_json = json.loads(data)
        
        if 'text' in data_json:
            print data_json['text']
            user = data_json['user']['screen_name']
            str = data_json['text']
            
            # If-statement after search() tests if it succeeded
            if find_words(str):                     
                print 'Found is true'
                message = twilioCli.messages.create(body='@' + user + ': ' + str, from_=myTwilioNumber, to=myCellPhone)
            else:
                print 'Found is false'
        print ""
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
    #stream.filter(track=['python', 'javascript', 'ruby'])
    stream.userstream(encoding='utf8')
