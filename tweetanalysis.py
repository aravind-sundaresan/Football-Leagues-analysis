from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import string
import pylab


if __name__ == '__main__':

    
    tweets_data_path_epl = 'tweetdata.txt'
    tweets = pd.DataFrame()
    
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")

    
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
            
        except:
            continue

    #print tweets_data
    print tweets_data

   

    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

    tweets_by_lang = tweets['lang'].value_counts()
    #print(tweets_by_lang)

    #graph to indicate the top 5 languages in which tweets were written
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Languages', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
    tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
    #pylab.show()

    tweets_by_country = tweets['country'].value_counts()

    #graph to indicate the top 5 countries from which tweets were sent 
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Countries', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
    tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
    pylab.show()
    
    tweets['NapoliJuve'] = tweets['text'].apply(lambda tweet: word_in_text('NapoliJuve', tweet))
    tweets['FCBAtleti'] = tweets['text'].apply(lambda tweet: word_in_text('FCBAtleti', tweet))
    tweets['MUNSOU'] = tweets['text'].apply(lambda tweet: word_in_text('MUNSOU', tweet))

    print "Number of Napoli vs Juve tweets: " + str(tweets['NapoliJuve'].value_counts()[True])
    print "Number of Barcelona vs Atleti tweets: " + str(tweets['FCBAtleti'].value_counts()[True])
    print "Number of Manchester United vs Saints tweets: " + str(tweets['MUNSOU'].value_counts()[True])

    leagues=['NapoliJuve','FCBAtleti','MUNSOU']
    
    tweets_by_league=[tweets['NapoliJuve'].value_counts()[True],tweets['FCBAtleti'].value_counts()[True],tweets['MUNSOU'].value_counts()[True]]
    x_pos = list(range(len(leagues)))
    
    width = 0.8
    fig, ax = plt.subplots()
    plt.bar(x_pos, tweets_by_league, 0.8, alpha=1, color='g')

    # Setting axis labels and ticks
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Ranking: NapoliJuve vs. FCBAtleti vs. MUNSOU', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(leagues)
    plt.grid()
    pylab.show()

    

