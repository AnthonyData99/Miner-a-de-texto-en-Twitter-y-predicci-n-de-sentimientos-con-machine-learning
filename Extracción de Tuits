import pandas as pd
import snscrape.modules.twitter as sntwitter

query ="(#pedrocastillo) lang:es until:2022-08-31 since:2022-01-01"
tweets=[]
limit=1000000
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
   
     #print(vars(tweet))
     # #break

    if len(tweets)== limit :
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df= pd.DataFrame(tweets, columns=["Date","User","Tweet"])
print(df)
df.to_csv("tweets_enero_agosto.csv")
