from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import string
import pylab
# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#listener thatprints received tweets to stdout.
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

    #This line filters Twitter Streams to capture data by the keywords e.g: #NapoliJuve,#FCBAtleti 
    #Write the tweets onto a file by using '> tweetdata.txt' when running this script
    stream.filter(track=[])


    