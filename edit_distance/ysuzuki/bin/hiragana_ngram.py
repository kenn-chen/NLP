#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
import math,re,datetime
import tweet
import ngram

def hiragana_ngram_learn(date,max_n):
    ngram_list = []
    for i in range(1,max_n+1):
        ngram_list.append(ngram.ngram(n=i,minimum=1))
    raw_tweets = tweet.raw_tweet([date])
    for raw_tweet in raw_tweets:
        t = tweet.tweet(raw_tweet)
        if t.tweettype == "T":
            matchlist = re.findall(u"[ぁ-んァ-ンｧ-ﾝ]+",t.text.decode("utf8"))
            if matchlist:
                for pattern in matchlist:
                    for ng in ngram_list:
                        ng.append(pattern)
    
    for ng in ngram_list:
        ng.make_ranking(write_flag=True)

if __name__ == "__main__":
    date = sys.argv[1]
    max_n = int(sys.argv[2])
    hiragana_ngram_learn(date = date,max_n = max_n)