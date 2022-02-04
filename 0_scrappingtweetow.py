# -*- coding: utf-8 -*-
"""0.ScrappingTweetow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14VMqCL84RFP_svnHVl758A_fmjosiW0T

Podłączam dysk
"""

from google.colab import drive
drive.mount('/content/drive/')

# use tweepy to scrap tweets
!pip install tweepy

import tweepy
import pickle
import time
import pandas as pd
import numpy as np

consumer_key = "XXX"
consumer_secret = "XXX"
access_token = "XXX"
access_token_secret = "XXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets_ids = pd.read_csv('/content/pl_covid_tweets_clean.txt', sep='\t')
tweets_ids

# Pobieranie tweetów po 50k
tweets = []
for k in range(11):
    for i in range(500*k,500*(k+1)):
        tweets_statuses = api.statuses_lookup(list(tweets_ids['tweet_id'][(i*100):(i*100+100)]))
        for i in range(len(tweets_statuses)):
            tweets.append(tweets_statuses[i].text)
    with open(f'/content/drive/MyDrive/ZUM/tweets_{50000*(k+1)}.pkl', 'wb') as f:
        pickle.dump(tweets, f)
    print(f'Pobrano {50000*(k+1)}/500000.')
    time.sleep(950)


len(tweets)

pd.DataFrame(tweets)

import os
import pandas as pd
import regex as re

data_path = '/content/drive/MyDrive/ZUM/'
for path in os.listdir(data_path):
    my_tweets = []
    df = pd.read_pickle(data_path + path)
    for tweet in df.tweet:
        url = re.findall(r"http\S+", tweet)
        if url == []:
            my_tweets.append(tweet)
    new_df = pd.DataFrame({"tweets": my_tweets, "author": path.replace(".pkl", "")})  # path[:-4]
    new_df.to_csv("/content/drive/My Drive/ZUM/tweets2.csv", index=False, mode="a", )

pd.DataFrame(tweets).to_csv('/content/drive/MyDrive/ZUM/tweets_data.csv')

"""Instaluję spacy"""

#!python -m pip install spacy==2.3.2 -q
#2.3.2,  żeby był w tym polski

# !python -m spacy download pl_core_news_md
#!python -m spacy download en_core_web_md

"""#Import bibliotek"""

from IPython.display import clear_output
!pip install twarc #Twarc
!pip install tweepy # Tweepy 3.8.0
!pip install argparse #Argparse 3.2
!pip install xtract #Xtract 0.1 a3
!pip install wget #Wget 3.2
clear_output()

source_list = '/content/pl_covid_tweets_clean.txt'

api = tweepy.API(auth, wait_on_rate_limit=True)
